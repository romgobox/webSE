#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from flask import request
from flask.views import MethodView
from webSE.api.decorators import user_required
from webSE.api.model.channels_type import get_channels_type


class ChannelsTypeAPI(MethodView):
    decorators = [user_required]

    def get(self, channels_type_id):
        if channels_type_id is None:
            response = get_channels_type()
            return json.dumps(response)
        else:
            id = int(channels_type_id)
            response = get_channels_type(id)
            return json.dumps(response)

    def post(self):
        pass

    def put(self, protocol_id):
        pass

    def delete(self, protocol_id):
        pass