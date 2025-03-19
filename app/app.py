from kafka import KafkaConsumer
import time
import logging

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    # logger.info("Starting 'python-app'...")
    # while True:
    #     logger.info("This message is printed every 5 seconds.")
    #     time.sleep(5)

    logger.info("Starting 'python-app'...")
    consumer = KafkaConsumer(
        'k6-metrics',                                     # Topic Name
        bootstrap_servers=['kafka:9092'],                # Connect to Kafka on the host
        auto_offset_reset='earliest',                    # Start reading from the beginning if there is no offset
        enable_auto_commit=False,                        # Disable autocommit
        group_id='k6-consumer-group'                     # Consumer group ID
    )
    try:
        logger.info("Listening to Kafka topic 'k6-metrics'...")
        for message in consumer:
            logger.info("Message processing...")

            logger.info(f"Received message: {message.value.decode('utf-8')}")

            logger.info("offset commit")
            consumer.commit()
    except KeyboardInterrupt:
        logger.error("Shutting down...")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()