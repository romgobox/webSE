#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request
from flask.views import MethodView
from webSE.api.model.channels import get_channels, add_channel, update_channel, del_channel


class ChannelsAPI(MethodView):

    def get(self, channel_id):
        if channel_id is None:
            response = get_channels()
            return json.dumps(response)
        else:
            id = int(channel_id)
            response = get_channel(id)
            return json.dumps(response)

    def post(self):
        data = {}
        data['ch_desc'] = request.json['ch_desc']
        data['ch_ip'] = request.json['ch_ip']
        data['ch_port'] = int(request.json['ch_port'])
        data['ch_settings'] = request.json['ch_settings']
        data['is_activ'] = int(request.json['is_activ'])
        response = add_channel(data)
        return json.dumps(response)

    def put(self, channel_id):
        id = int(channel_id)
        data = {}
        data['ch_desc'] = request.json['ch_desc']
        data['ch_ip'] = request.json['ch_ip']
        data['ch_port'] = int(request.json['ch_port'])
        data['ch_settings'] = request.json['ch_settings']
        data['is_activ'] = int(request.json['is_activ'])
        response = update_channel(id, data)
        return json.dumps(response)

    def delete(self, channel_id):
        id = int(channel_id)
        response = del_channel(id)
        return json.dumps(response)