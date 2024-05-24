from confluent_kafka import Consumer, KafkaError
from django.conf import settings

def kafka_consumer():
    c = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    })
    
    c.subscribe(['test-topic'])
    
    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        print(f'Received message: {msg.value().decode("utf-8")}')
    
    c.close()

if __name__ == "__main__":
    kafka_consumer()
