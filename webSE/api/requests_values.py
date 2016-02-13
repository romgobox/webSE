#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
import gevent.monkey
from flask import request
from webSE import app
from SE30x.algorithm import Algorithm
gevent.monkey.patch_socket()


@app.route('/requests/channels', methods=['POST'])
def requests_by_channels():
    channels = request.json['channels']
    alg_type = request.json['alg_type']

    def run_algorithm(channel):
        algorithm = Algorithm(channels_id=[channel], alg_type='full')
        return algorithm.requestResult

    requests = [gevent.spawn(run_algorithm, channel) for channel in channels]
    gevent.joinall(requests)
    response = []
    for greenlet in requests:
        response.append(greenlet.value)
    return json.dumps(response)