#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request, g
from flask.views import MethodView
from webSE.api.decorators import user_required
from webSE.api.model.channels import get_channels, add_channel, update_channel, del_channel


class ChannelsAPI(MethodView):
    decorators = [user_required]

    def get(self, channel_id):
        user_id = g.user or None
        if channel_id is None:
            response = get_channels(user_id)
            return json.dumps(response)
        else:
            id = int(channel_id)
            response = get_channel(id)
            return json.dumps(response)

    def post(self):
        user_id = g.user or None
        data = {}
        data['ch_desc'] = request.json['ch_desc']
        data['ch_ip'] = request.json['ch_ip']
        data['type_id'] = int(request.json['type_id'])
        data['ch_port'] = int(request.json['ch_port'])
        data['ch_settings'] = request.json['ch_settings']
        data['is_active'] = int(request.json['is_active'])
        response = add_channel(data, user_id)
        return json.dumps(response)

    def put(self, channel_id):
        user_id = g.user or None
        id = int(channel_id)
        data = {}
        data['ch_desc'] = request.json['ch_desc']
        data['ch_ip'] = request.json['ch_ip']
        data['type_id'] = int(request.json['type_id'])
        data['ch_port'] = int(request.json['ch_port'])
        data['ch_settings'] = request.json['ch_settings']
        data['is_active'] = int(request.json['is_active'])
        response = update_channel(id, data, user_id)
        return json.dumps(response)

    def delete(self, channel_id):
        user_id = g.user or None
        id = int(channel_id)
        response = del_channel(id, user_id)
        return json.dumps(response)