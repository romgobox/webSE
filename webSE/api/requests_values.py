#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
import gevent.monkey
from flask import request
from webSE import app
from SE30x.algorithm import Algorithm
gevent.monkey.patch_socket()



def alg_run(channel):
    # global result
    algorithm = Algorithm(channels_id=[channel], alg_type='full')
    # result.append(algorithm.requestResult)
    return algorithm.requestResult

def main():   
    channels = [11,9]

    requests = [gevent.spawn(alg_run, channel) for channel in channels]
    gevent.joinall(requests)
    # algorithm = Algorithm(channels_id=[12, 9], alg_type='full')
    # result = algorithm.requestResult
    import pudb; pu.db

if __name__ == '__main__':
    result = []
    main()

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