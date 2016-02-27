#! /usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify, g, redirect, url_for
from flask.ext.login import login_required
import json
import os
import ConfigParser
import webSE.api.model
from webSE.api.meters import MetersAPI
from webSE.api.objects import ObjectsAPI
from webSE.api.channels import ChannelsAPI
from webSE.api.protocols import ProtocolsAPI
from webSE.api.meters_type import MetersTypeAPI
from webSE.api.channels_type import ChannelsTypeAPI
from webSE.api.channels_status import ChannelsStatusAPI

config_file = os.path.dirname(__file__)+'/config.ini'
parser = ConfigParser.SafeConfigParser()
parser.read(config_file)

app = Flask(__name__)
app.config['SECRET_KEY'] = parser.get('app', 'SECRET_KEY')

import webSE.api.login
import webSE.api.reports
import webSE.api.requests_values


@app.route('/webamr')
@login_required
def webamr_index():
    return render_template('base.html')


meters_view = MetersAPI.as_view('meters_api')
app.add_url_rule('/meters', defaults={'meter_id': None}, view_func=meters_view, methods=['GET',])
app.add_url_rule('/meters', view_func=meters_view, methods=['POST',])
app.add_url_rule('/meters/<int:meter_id>', view_func=meters_view, methods=['GET', 'PUT', 'DELETE'])

meters_type_view = MetersTypeAPI.as_view('meters_type_api')
app.add_url_rule('/meters_type', defaults={'meters_type_id': None}, view_func=meters_type_view, methods=['GET',])

channels_view = ChannelsAPI.as_view('channels_api')
app.add_url_rule('/channels', defaults={'channel_id': None}, view_func=channels_view, methods=['GET',])
app.add_url_rule('/channels', view_func=channels_view, methods=['POST',])
app.add_url_rule('/channels/<int:channel_id>', view_func=channels_view, methods=['GET', 'PUT', 'DELETE'])

channels_type_view = ChannelsTypeAPI.as_view('channels_type_api')
app.add_url_rule('/channels_type', defaults={'channels_type_id': None}, view_func=channels_type_view, methods=['GET',])

channels_status_view = ChannelsStatusAPI.as_view('channels_status_api')
app.add_url_rule('/channels_status', defaults={'channel_id': None}, view_func=channels_status_view, methods=['GET'])
app.add_url_rule('/channels_status/<int:channel_id>', view_func=channels_status_view, methods=['GET', 'PUT'])

objects_view = ObjectsAPI.as_view('objects_api')
app.add_url_rule('/objects', defaults={'object_id': None}, view_func=objects_view, methods=['GET',])
app.add_url_rule('/objects', view_func=objects_view, methods=['POST',])
app.add_url_rule('/objects/<int:object_id>', view_func=objects_view, methods=['GET', 'PUT', 'DELETE'])

protocols_view = ProtocolsAPI.as_view('protocols_api')
app.add_url_rule('/protocols', defaults={'protocol_id': None}, view_func=protocols_view, methods=['GET',])

