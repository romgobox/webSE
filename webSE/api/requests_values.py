#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request
from webSE import app
from SE30x.algorithm import Algorithm

@app.route('/requests/channels', methods=['POST'])
def requests_by_channels():
    channels = request.json['channels']
    alg_type = request.json['alg_type']
    algorithm = Algorithm(channels_id=channels, alg_type=alg_type)
    response = algorithm.requestResult
    return json.dumps(response)