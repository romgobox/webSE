#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from webSE.api.model import get_db

def get_meters(user_id=None):
    meters_sql = '''
    SELECT 
        wh.id, 
        wh.type_id, 
        wh.wh_adr, 
        wh.wh_num, 
        wh.wh_pass, 
        wh.wh_desc, 
        wh.wh_ki,
        wh.wh_ku,
        wh.wh_impl,
        wh.wh_settings, 
        wh.object_id,
        wh.channel_id,
        wh.is_active
    FROM 
        meters wh
    WHERE user_id={user_id}
    ORDER BY wh.object_id
    '''.format(user_id=user_id)

    cur, con = get_db()
    cur.execute(meters_sql)
    meters = cur.fetchall()
    meters_list = []
    for row in meters:
        meter = dict(row)
        meters_list.append(meter)
    return meters_list

def add_meter(data, user_id=None):
    meter_sql = u'''
    INSERT INTO meters 
    VALUES(
        DEFAULT,
        {type_id}, 
        '{wh_adr}', 
        '{wh_num}',
        '{wh_pass}',  
        '{wh_desc}', 
        {wh_ki},
        {wh_ku},
        {wh_impl},
        '{wh_settings}', 
        {object_id}, 
        {channel_id}, 
        {is_active},
        {user_id})
    RETURNING id
    '''.format(
            type_id=data['type_id'],
            wh_adr=data['wh_adr'], 
            wh_num=data['wh_num'], 
            wh_pass=data['wh_pass'], 
            wh_desc=data['wh_desc'],
            wh_ki=data['wh_ki'],
            wh_ku=data['wh_ku'],
            wh_impl=data['wh_impl'],
            wh_settings=json.dumps(data['wh_settings']), 
            object_id=data['object_id'],
            channel_id=data['channel_id'], 
            is_active=data['is_active'],
            user_id=user_id)

    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(meter_sql)
        con.commit()
        data['id'] = cur.fetchone()['id']
        response = data
        response['status'] = u'Добавлен новый прибор учета'
    except Exception, e:
        response['status'] = u'Прибор учета не добавлен. Причина: {e}'.format(e=e)
    return response

def update_meter(whID, data, user_id=None):
    meter_sql = u'''
    UPDATE meters
    SET 
        type_id={type_id},
        wh_adr='{wh_adr}', 
        wh_num='{wh_num}', 
        wh_pass='{wh_pass}', 
        wh_desc='{wh_desc}',
        wh_ki={wh_ki},
        wh_ku={wh_ku},
        wh_impl={wh_impl},
        wh_settings='{wh_settings}', 
        object_id={object_id},
        channel_id={channel_id}, 
        is_active={is_active},
        user_id={user_id}
    WHERE id={id}
    '''.format(
            type_id=data['type_id'],
            wh_adr=data['wh_adr'], 
            wh_num=data['wh_num'], 
            wh_pass=data['wh_pass'], 
            wh_desc=data['wh_desc'],
            wh_ki=data['wh_ki'],
            wh_ku=data['wh_ku'],
            wh_impl=data['wh_impl'],
            wh_settings=json.dumps(data['wh_settings']),
            object_id=data['object_id'],
            channel_id=data['channel_id'], 
            is_active=data['is_active'],
            user_id=user_id,
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

def del_meter(id, user_id=None):
    meter_sql = u'''
    DELETE FROM meters
    WHERE id={id} AND user_id={user_id}
    '''.format(id=id, user_id=user_id)
    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(meter_sql)
        con.commit()
        response['status'] = u'Удален прибор учета'
    except Exception, e:
        response['status'] = u'Прибор учета не удален. Причина: {e}'.format(e=e)
    return response