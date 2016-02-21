#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from webSE.api.model import get_db

def get_meters():
    meters_sql = '''
    SELECT 
        wh.id, 
        wh.type_id, 
        wh.wh_adr, 
        wh.wh_num, 
        wh.wh_pass, 
        wh.wh_desc, 
        wh.wh_KI, 
        wh.wh_KU, 
        wh.wh_IMPL, 
        wh.wh_settings, 
        wh.object_id,
        wh.channel_id,
        wh.is_active
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
        {type_id}, 
        '{wh_adr}', 
        '{wh_num}',
        '{wh_pass}',  
        '{wh_desc}', 
        {wh_KI}, 
        {wh_KU}, 
        {wh_IMPL}, 
        '{wh_settings}', 
        {object_id}, 
        {channel_id}, 
        {is_active})
    '''.format(
            type_id=data['type_id'],
            wh_adr=data['wh_adr'], 
            wh_num=data['wh_num'], 
            wh_pass=data['wh_pass'], 
            wh_desc=data['wh_desc'],
            wh_KI=data['wh_KI'], 
            wh_KU=data['wh_KU'], 
            wh_IMPL=data['wh_IMPL'],  
            wh_settings=json.dumps(data['wh_settings']), 
            object_id=data['object_id'],
            channel_id=data['channel_id'], 
            is_active=data['is_active'])

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
        type_id={type_id},
        wh_adr='{wh_adr}', 
        wh_num='{wh_num}', 
        wh_pass='{wh_pass}', 
        wh_desc='{wh_desc}',
        wh_KI={wh_KI}, 
        wh_KU={wh_KU}, 
        wh_IMPL={wh_IMPL}, 
        wh_settings='{wh_settings}', 
        object_id={object_id},
        channel_id={channel_id}, 
        is_active={is_active}
    WHERE id={id}
    '''.format(
            type_id=data['type_id'],
            wh_adr=data['wh_adr'], 
            wh_num=data['wh_num'], 
            wh_pass=data['wh_pass'], 
            wh_desc=data['wh_desc'],
            wh_KI=data['wh_KI'], 
            wh_KU=data['wh_KU'], 
            wh_IMPL=data['wh_IMPL'],  
            wh_settings=json.dumps(data['wh_settings']), 
            object_id=data['object_id'],
            channel_id=data['channel_id'], 
            is_active=data['is_active'],
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