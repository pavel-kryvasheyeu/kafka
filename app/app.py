from kafka import KafkaConsumer
import logging
import time

from kafka.errors import NoBrokersAvailable

KAFKA_TOPICS = 'k6-metrics'
KAFKA_BOOTSTRAP_SERVERS = ['kafka:9092'] # Kafka connect host
AUTO_OFFSET_RESET = 'earliest' # Start reading from the beginning if there is no offset
IS_AUTOCOMMIT_ENABLED = False
KAFKA_CONSUMER_GROUP_ID = 'k6-consumer-group'

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def wait_for_kafka():
    while True:
        try:
            consumer = KafkaConsumer(
                KAFKA_TOPICS,
                bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS,
                auto_offset_reset = AUTO_OFFSET_RESET,
                enable_auto_commit = IS_AUTOCOMMIT_ENABLED,
                group_id = KAFKA_CONSUMER_GROUP_ID
            )
            return consumer
        except NoBrokersAvailable:
            log.warning("Kafka broker not available, retrying in 5 seconds...")
            time.sleep(5)

def main():
    log.info("Starting 'python-app'...")
    consumer = wait_for_kafka()
    try:
        log.info("Listening to Kafka topic 'k6-metrics'...")
        for message in consumer:
            log.info("Message processing...")

            log.info(f"Received message: {message.value.decode('utf-8')}")

            log.info("offset commit")
            consumer.commit()
    except KeyboardInterrupt:
        log.error("Shutting down...")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()