#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request
from flask.views import MethodView
from webSE.api.model.channels_status import get_channels_status, get_channel_status


class ChannelsStatusAPI(MethodView):

    def get(self, channel_id):
        if channel_id is None:
            response = get_channels_status()
            return json.dumps(response)
        else:
            id = int(channel_id)
            response = get_channel_status(channel_id=id)
            return json.dumps(response)

    def post(self):
        pass

    def put(self, protocol_id):
        pass

    def delete(self, protocol_id):
        pass