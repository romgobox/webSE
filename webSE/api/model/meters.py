#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from webSE.api.model import get_db

def get_meters():
    meters_sql = '''
    SELECT 
        wh.id, 
        wh.wh_adr, 
        wh.wh_num, 
        wh.wh_pass, 
        wh.object_id,
        wh.wh_desc, 
        wh.wh_settings, 
        wh.protocol_id, 
        wh.channel_id
    FROM 
        meters wh
    ORDER BY wh.object_id
    '''
    cur, con = get_db()
    cur.execute(meters_sql)
    meters = cur.fetchall()
    meters_list = []
    for row in meters:
        meter = dict(row)
        meter['wh_settings'] = json.loads(meter['wh_settings'])
        meters_list.append(meter)
    return meters_list

def add_meter(data):
    meter_sql = u'''
    INSERT INTO meters 
    VALUES(
        Null,
        '{wh_adr}', 
        '{wh_num}',
        '{wh_pass}',  
        {object_id}, 
        '{wh_desc}', 
        '{wh_settings}', 
        {protocol_id}, 
        {channel_id})
    '''.format(
            wh_adr=data['wh_adr'], 
            wh_num=data['wh_num'], 
            wh_pass=data['wh_pass'], 
            object_id=data['object_id'],
            wh_desc=data['wh_desc'], 
            wh_settings=json.dumps(data['wh_settings']), 
            protocol_id=data['protocol_id'],
            channel_id=data['channel_id'])

    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(meter_sql)
        con.commit()
        data['id'] = cur.lastrowid
        response = data
        response['status'] = u'Добавлен новый прибор учета'
    except Exception, e:
        response['status'] = u'Прибор учета не добавлен. Причина: {e}'.format(e=e)
    return response

def update_meter(whID, data):
    meter_sql = u'''
    UPDATE meters
    SET 
        wh_adr='{wh_adr}', 
        wh_num='{wh_num}', 
        wh_pass='{wh_pass}', 
        object_id={object_id},
        wh_desc='{wh_desc}', 
        wh_settings='{wh_settings}', 
        protocol_id={protocol_id},
        channel_id={channel_id}
    WHERE id={id}
    '''.format(
            wh_adr=data['wh_adr'], 
            wh_num=data['wh_num'], 
            wh_pass=data['wh_pass'], 
            object_id=data['object_id'],
            wh_desc=data['wh_desc'], 
            wh_settings=json.dumps(data['wh_settings']), 
            protocol_id=data['protocol_id'],
            channel_id=data['channel_id'],
            id=whID)

    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(meter_sql)
        con.commit()
        response['status'] = u'Сохранено'
    except Exception, e:
        response['status'] = u'Не сохранено. Причина: {e}'.format(e=e)
    return response

def del_meter(id):
    meter_sql = u'''
    DELETE FROM meters
    WHERE id={id}
    '''.format(id=id)
    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(meter_sql)
        con.commit()
        response['status'] = u'Удален прибор учета'
    except Exception, e:
        response['status'] = u'Прибор учета не удален. Причина: {e}'.format(e=e)
    return response