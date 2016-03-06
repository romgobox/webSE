#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import json
import logging
from datetime import datetime
from webSE.protocol.se30x import SE30X, ProtocolFactory
from webSE.protocol.tcp_channel import ChannelFactory
from webSE.protocol.utils import dateList, dateListPP
from webSE.api.model import get_db
from webSE.api.model.channels_status import update_channel_status
from meter import Meter
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-4s [%(asctime)s] %(message)s', level = logging.DEBUG)


class Algorithm(object):
    """Класс алгоритма опроса"""

    def __init__(self, channels_id=[], meters_id=[], alg_type='full'):
        self.metersMap = {}
        self.channels = []
        self.channels_id = channels_id or []
        self.meters_id = meters_id or []
        self.alg_type = alg_type or 'full'
        self.requestResult = self.runAlgorithm(self.alg_type)

    def runAlgorithm(self, alg_type):
        result = None
        if alg_type == 'full':
            if self.channels_id:
                for channel in self.channels_id:
                    self.getMetersByChannel(ch_id=channel)
                self.fullAlgorithm()
                self.saveValues('full')
                result = self.serializeValues('full')

        return result

    def fullAlgorithm(self):
        for channel, meters in self.metersMap.items():
            update_channel_status(channel_id=channel.id, status_code=1)
            try:
                channel.connect()
                update_channel_status(channel_id=channel.id, status_code=2)
            except:
                update_channel_status(channel_id=channel.id, status_code=5)
                break
            for meter in meters:
                update_channel_status(channel_id=channel.id, status_code=3)
                params = meter.parameters
                if meter.authCheckNum():
                    if params.get('fixDay'):
                        depth = int(params['fixDay'])
                        dates = meter.checkFixDayValInDB(depth)
                        meter.getFixedValues(dates)
                    if params.get('ppValue'):
                        depth = int(params['ppValue'])
                        meter.getppValueMap(depth)
                        dates = meter.checkPPValueValInDB(depth)
                        meter.getPPValues(dates)
                meter.logOut()
            channel.terminate()
            update_channel_status(channel_id=channel.id, status_code=4)

    def getMetersByChannel(self, ch_id=None, channel=None):
        channel = channel or self.getChannel(ch_id)
        ch_id = ch_id or channel.id
        meters_sql = '''
            SELECT 
                wh.id, 
                wh.wh_adr, 
                wh.wh_num, 
                wh.wh_pass, 
                wh.wh_settings, 
                pr.short_type pr_name
            FROM meters wh, meters_type mt, protocols pr
            WHERE wh.channel_id={ch_id} AND wh.type_id=mt.id AND mt.protocol_id=pr.id;
            '''.format(ch_id=ch_id)

        cur, con = get_db()
        cur.execute(meters_sql)
        meters = cur.fetchall()
        for meter in meters:
            mid = meter['id']
            madr = meter['wh_adr']
            mnum = meter['wh_num']
            mpass = meter['wh_pass']
            params = meter['wh_settings']
            protocol = meter['pr_name']
            meter = Meter(mid, madr, mnum, mpass, protocol=ProtocolFactory.get_protocol(protocol), 
                                                            channel=channel, parameters=params)
            if self.metersMap.get(channel):
                self.metersMap[channel].append(meter)
            else:
                self.metersMap[channel] = [meter]

    def getChannel(self, ch_id):
        channel_sql = '''
            SELECT 
                ch.id, 
                ch.ch_ip, 
                ch.ch_port,
                ct.short_type 
            FROM channels ch, channels_type ct
            WHERE ch.id={ch_id} AND ch.is_active=1 AND ch.type_id=ct.id
            '''.format(ch_id=ch_id)
        cur, con = get_db()
        cur.execute(channel_sql)
        result = cur.fetchone()
        id = result['id']
        ch_ip = result['ch_ip']
        ch_port = result['ch_port']
        ch_type = 'TCPClient'
        channelFactory = ChannelFactory(id=id, ch_ip=ch_ip, ch_port=ch_port, ch_type=ch_type)
        channel = channelFactory.getChannel()
        self.channels.append(channel)
        return channel

    def saveValues(self, alg_type):
        if alg_type == 'full':
            for meters in self.metersMap.values():
                for meter in meters:
                    meter.saveFixDayValues()
                    meter.saveppValues()


    def serializeValues(self, alg_type):
        if alg_type == 'full':
            result = []
            for meters in self.metersMap.values():
                for meter in meters:
                    row = {
                        'id':meter.id,
                        'fixDay':meter.fixDayValue,
                        'ppValue':meter.ppValue
                    }
                    result.append(row)

        return result
