#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.1.1'))
channel = connection.channel()

queue = raw_input("Para quem vai a mensagem? ")

channel.queue_declare(queue)

text = raw_input("Texto a ser enviado: ")

channel.basic_publish(exchange='',
                      routing_key=queue,
                      body=text)
print(" [x] Sent to 	"+queue)
print(" [x] Sent 	"+text)

connection.close()
