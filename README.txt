Kafka docker images
-------------------
* Off image (currently in use) https://kafka.apache.org/downloads:
https://hub.docker.com/r/apache/kafka
docker run -d -p 9092:9092 --name broker apache/kafka:latest
docker run -d -p 9092:9092 --name broker -e KAFKA_NODE_ID=1 -e KAFKA_PROCESS_ROLES=broker,controller -e KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@localhost:9093 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1 -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0 -e KAFKA_NUM_PARTITIONS=3 apache/kafka:latest

docker build -t python-kafka-app .
docker run --rm -it --name python-app python-kafka-app

* Confluent image:
https://docs.confluent.io/platform/current/installation/docker/config-reference.html
docker run -d --name=kafka-kraft -h kafka-kraft -p 9101:9101 -e KAFKA_NODE_ID=1 -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka-kraft:29092,PLAINTEXT_HOST://localhost:9092 -e KAFKA_JMX_PORT=9101 -e KAFKA_JMX_HOSTNAME=localhost -e KAFKA_PROCESS_ROLES=broker,controller -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@kafka-kraft:29093 -e KAFKA_LISTENERS=PLAINTEXT://kafka-kraft:29092,CONTROLLER://kafka-kraft:29093,PLAINTEXT_HOST://0.0.0.0:9092 -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER -e CLUSTER_ID=MkU3OEVBNTcwNTJENDM2Qk confluentinc/cp-kafka:7.9.0

bash
--------------
check listening on port 9092 for windows
netstat -ano | findstr 9092

docker
---------------
docker exec -it kafka /bin/bash
cd /opt/kafka/bin

kafka-cli
---------------
put:
./kafka-console-producer.sh --bootstrap-server localhost:9092 --topic k6-metrics

poll:
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic k6-metrics --from-beginning
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic k6-metrics --from-beginning --group k6-consumer-group
