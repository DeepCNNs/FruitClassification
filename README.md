# FruitClassification

This is a complete end to end application to classify fruits (Apple, Banana, Orange)

## Installation on Ubuntu

1. Tensorflow
pip install tensorflow-gpu

2. Kafka
Download the latest Kafka release (https://www.apache.org/dyn/closer.cgi?path=/kafka/2.7.0/kafka_2.13-2.7.0.tgz) and extract it:
tar -xzf kafka_2.13-2.7.0.tgz
cd kafka_2.13-2.7.0

3. Python opencv: 
https://docs.opencv.org/master/d2/de6/tutorial_py_setup_in_ubuntu.html

4. configparser: 
pip install configparser 

5. Flask: 
pip install Flask

6. Numpy: 
pip install numpy

7. Matplotlib: 
pip install matplotlib

## Setup

1. Start Kafka: 
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

2. Create Kafka topic: 
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic assignment-input
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic assignment-output

3. Start Listener:
export PYTHONPATH="${PYTHONPATH}:$PROJECT_HOME"
python3 src/algorithm/listener.py

4. Start Service:
export PYTHONPATH="${PYTHONPATH}:$PROJECT_HOME"
python3 src/service/service.py

## Test
Run following test file from Project home
python3 tests/client.py

