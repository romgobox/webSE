#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
import logging
import random
import gevent.monkey
from flask import request
from webSE import app
from SE30x.algorithm import Algorithm
from kombu import Connection, Exchange, Queue, Producer, Consumer
gevent.monkey.patch_socket()
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-4s [%(asctime)s] %(message)s', level = logging.DEBUG)

def publishRequest(channels, alg_type, reply=False):

    reply_rk = ''
    if reply:
        reply_hash = str(random.random())
        reply_queue = 'reply_queue_' + reply_hash
        reply_rk = 'reply_rk_' + reply_hash

    message = json.dumps({
        'channels':channels,
        'alg_type':alg_type,
        'reply_rk': reply_rk
    })
    with Connection() as connection:
        exc_name = 'requests'
        rk_name = 'full'
        channel = connection.channel()
        exchange = Exchange(name=exc_name, channel=channel, type='direct', auto_delete=True)
        producer = Producer(channel=channel, exchange=exchange, routing_key=rk_name)
        producer.publish(message, routing_key=rk_name)

    response = {}
    response['message'] = u'Задание на опрос добавлено в очередь!'
    if reply:
        response['result'] = consumeResponse(reply_queue, reply_rk)
    return response

def consumeResponse(queue, routing_key):

    response = []

    def on_message(body, message):
        response.append(json.loads(body))
        logging.debug(u'Получен результат опроса')
        message.ack()

    exc_name = 'requests'
    with Connection() as connection:
        channel = connection.channel()
        exchange = Exchange(name=exc_name, channel=channel, type='direct', auto_delete=True)
        queue = Queue(name=queue, channel=channel, exchange=exchange, routing_key=routing_key, 
                                                            auto_delete=True, exclusive=True)
        queue.bind(channel=channel)
        try:
            with Consumer(
                connection,
                queues=(queue, ),
                callbacks=(on_message, ),
            ):
                while not response:
                    connection.drain_events()
                    gevent.sleep()
        except KeyboardInterrupt:
            pass
    
    if response:
        return response[0]