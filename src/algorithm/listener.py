from classifier import Classifier
from kafka import KafkaConsumer
from kafka import KafkaProducer
from src.common import read_image
from src.config_manager import listener_topic, model_path, kafka_uri, service_topic

debug = True

# Listener listens to the kafka queue for
class Listener:
    def __init__(self):
        self.consumer = KafkaConsumer(listener_topic)
        self.classifier_obj = Classifier(model_path)
        self.producer = KafkaProducer(bootstrap_servers=[kafka_uri])
    
    def run(self):
        while True:
            # wait for inference requests
            for message in self.consumer:
                if debug:
                    print (message)
                # read image
                image = read_image(message.value.decode('ascii'))
                
                # predict
                pred = self.classifier_obj.predict(image)
                
                # send the response back to kafka queue
                self.producer.send(service_topic, key=str(message.key.decode('ascii')).encode('ascii'), value=pred.encode('ascii'))
                if debug:
                    print("response sent")
                
if __name__ == "__main__":
    listener_obj = Listener()
    listener_obj.run()