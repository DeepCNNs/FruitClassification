from flask import Flask, request
from kafka import KafkaProducer, KafkaConsumer
import json
from src.config_manager import listener_topic, kafka_uri, service_topic

app = Flask(__name__)
consumer = KafkaConsumer(service_topic)
producer = KafkaProducer(bootstrap_servers=kafka_uri)
count = 0
debug = True

@app.route("/")
def home():
    return "Server is up and running"

@app.route("/heartbeat")
def heartbeat():
    return "Server is up and running"
    
# API to run inference, accepts POST requests
@app.route("/identify-fruit", methods=['POST'])
def identify_fruit():
    data = json.loads(request.data)
    
    if debug:
        print("request received: ", data)
        
    producer.send(listener_topic, key=str(data['id']).encode('ascii'), value=data['img_path'].encode('ascii'))
    for message in consumer:
        if debug:
            print (message)
        if int(message.key.decode('ascii')) == data['id']:
            return json.dumps({"fruit_type": message.value.decode('ascii')})
    count += 1
    
if __name__ == "__main__":
    app.run(threaded=True,debug=True)
