#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
# import logging
# import random
# import gevent.monkey
from flask import request
from webSE import app
from webSE.algorithm import publishRequest, consumeResponse
# from SE30x.algorithm import Algorithm
# from kombu import Connection, Exchange, Queue, Producer, Consumer
# gevent.monkey.patch_socket()
# logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-4s [%(asctime)s] %(message)s', level = logging.DEBUG)


@app.route('/requests/channels', methods=['POST'])
def requests_by_channels():
    channels = request.json['channels']
    alg_type = request.json['alg_type']
    reply = request.json['reply']
    response = publishRequest(channels, alg_type, reply)
    return json.dumps(response)