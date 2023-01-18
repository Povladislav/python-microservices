import pika

params = pika.URLParameters('amqps://vpmyobkb:h7Y7q0LjHoyvS6_5DfAfmqiB0cdCmS8a@codfish.rmq.cloudamqp.com/vpmyobkb')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Receive in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback,auto_ack=True)
print('Started consuming')
channel.start_consuming()
channel.close()
