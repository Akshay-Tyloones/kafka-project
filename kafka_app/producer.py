from confluent_kafka import Producer
from django.conf import settings

def kafka_producer():
    p = Producer({'bootstrap.servers': settings.KAFKA_BROKER_URL})
    
    def delivery_report(err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')
    
    def produce_message(message):
        p.produce(settings.KAFKA_TOPIC, message.encode('utf-8'), callback=delivery_report)
        p.poll(1)
    
    return produce_message
