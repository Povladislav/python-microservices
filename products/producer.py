import pika, json

params = pika.URLParameters('amqps://vpmyobkb:h7Y7q0LjHoyvS6_5DfAfmqiB0cdCmS8a@codfish.rmq.cloudamqp.com/vpmyobkb')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
