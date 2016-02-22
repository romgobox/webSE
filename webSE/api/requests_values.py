#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request
from webSE import app
from webSE.algorithm import publishRequest, consumeResponse


@app.route('/requests/channels', methods=['POST'])
def requests_by_channels():
    channels = request.json['channels']
    alg_type = request.json['alg_type']
    reply = request.json['reply']
    response = publishRequest(channels, alg_type, reply)
    return json.dumps(response)
