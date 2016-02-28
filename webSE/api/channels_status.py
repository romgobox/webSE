#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request, g
from flask.views import MethodView
from webSE.api.decorators import user_required
from webSE.api.model.channels_status import get_channels_status, get_channel_status


class ChannelsStatusAPI(MethodView):
    decorators = [user_required]

    def get(self, channel_id):
        user_id = g.user or None
        if channel_id is None:
            response = get_channels_status(user_id)
            return json.dumps(response)
        else:
            id = int(channel_id)
            response = get_channel_status(channel_id=id, user_id=user_id)
            return json.dumps(response)

    def post(self):
        pass

    def put(self, protocol_id):
        pass

    def delete(self, protocol_id):
        pass
