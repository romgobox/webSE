#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gevent.monkey
gevent.monkey.patch_socket()

import logging
import json
from kombu import Connection, Exchange, Queue, Consumer, Producer
from SE30x.algorithm import Algorithm
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-4s [%(asctime)s] %(message)s', level = logging.DEBUG)


greenlets = {}
def async(fn):
    def _fn(*args, **kwargs):
        fn(*args, **kwargs)
        del greenlets[id(gevent.getcurrent())]

    def spawn_greenlet(*args, **kwargs):
        greenlet = gevent.spawn(_fn, *args, **kwargs)
        greenlets[id(greenlet)] = greenlet

    return spawn_greenlet


def publishResponse(response, rk_name):
    with Connection() as connection:
        exc_name = 'requests'
        message = json.dumps(response)
        channel = connection.channel()
        exchange = Exchange(name=exc_name, channel=channel, type='direct', auto_delete=True)
        producer = Producer(channel=channel, exchange=exchange, routing_key=rk_name)
        producer.publish(message, routing_key=rk_name)

@async
def on_message(body, message):
    request = json.loads(body)
    channels = request['channels']
    alg_type = request['alg_type']
    rk_name = request['reply_rk']
    logging.debug(u'Получено новое задание. Каналы: {channels} тип алгоритма: {alg_type}'.format(channels=channels, alg_type=alg_type))

    def run_algorithm(channel):
        algorithm = Algorithm(channels_id=[channel], alg_type=alg_type)
        return algorithm.requestResult

    requests = [gevent.spawn(run_algorithm, channel) for channel in channels]
    gevent.joinall(requests)
    response = []
    for greenlet in requests:
        response.append(greenlet.value)
    message.ack()
    if rk_name:
        publishResponse(response, rk_name)


def main():
    exc_name = 'requests'
    queue_name = 'alg'
    rk_name = 'full'
    with Connection() as connection:
        channel = connection.channel()
        exchange = Exchange(name=exc_name, channel=channel, type='direct', auto_delete=True)
        queue = Queue(name=queue_name, channel=channel, exchange=exchange, routing_key=rk_name, auto_delete=True)
        queue.bind(channel=channel)
        try:
            with Consumer(
                connection,
                queues=(queue, ),
                callbacks=(on_message, ),
            ):
                while True:
                    connection.drain_events()
                    gevent.sleep()
        except KeyboardInterrupt:
            pass
            gevent.joinall(greenlets.values())


if __name__ == '__main__':
    main()