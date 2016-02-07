#! /usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
import json
import webSE.api.model
from webSE.api.meters import MetersAPI
from webSE.api.channels import ChannelsAPI
from webSE.api.objects import ObjectsAPI
from webSE.api.protocols import ProtocolsAPI

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

import webSE.api.reports

meters_view = MetersAPI.as_view('meters_api')
app.add_url_rule('/meters', defaults={'meter_id': None}, view_func=meters_view, methods=['GET',])
app.add_url_rule('/meters', view_func=meters_view, methods=['POST',])
app.add_url_rule('/meters/<int:meter_id>', view_func=meters_view, methods=['GET', 'PUT', 'DELETE'])

channels_view = ChannelsAPI.as_view('channels_api')
app.add_url_rule('/channels', defaults={'channel_id': None}, view_func=channels_view, methods=['GET',])
app.add_url_rule('/channels', view_func=channels_view, methods=['POST',])
app.add_url_rule('/channels/<int:channel_id>', view_func=channels_view, methods=['GET', 'PUT', 'DELETE'])

objects_view = ObjectsAPI.as_view('objects_api')
app.add_url_rule('/objects', defaults={'object_id': None}, view_func=objects_view, methods=['GET',])
app.add_url_rule('/objects', view_func=objects_view, methods=['POST',])
app.add_url_rule('/objects/<int:object_id>', view_func=objects_view, methods=['GET', 'PUT', 'DELETE'])

protocols_view = ProtocolsAPI.as_view('protocols_api')
app.add_url_rule('/protocols', defaults={'protocol_id': None}, view_func=protocols_view, methods=['GET',])

