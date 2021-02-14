import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')    
    
model_path = config['CLASSIFIER']['model_path']
kafka_uri = config['KAFKA']['uri']
service_topic = config['SERVICE']['topic']
listener_topic = config['LISTENER']['topic']
