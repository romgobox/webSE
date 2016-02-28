#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
from webSE.api.model import get_db

def get_objects(user_id=None):
    objects_sql = '''
    SELECT
        obj.id, 
        obj.higher, 
        obj.obj_desc
    FROM
        objects obj
    WHERE user_id={user_id}
    '''.format(user_id=user_id)

    cur, con = get_db()
    cur.execute(objects_sql)
    objects = cur.fetchall()
    objects_list = []
    for row in objects:
        object_row = dict(row)
        objects_list.append(object_row)
    return objects_list

def add_object(data, user_id=None):
    object_sql = u'''
    INSERT INTO objects 
    VALUES(
        Null, 
        {higher},
        '{obj_desc}',
        {user_id})
    '''.format(obj_desc=data['obj_desc'],
                higher=data['higher'],
                user_id=user_id)

    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(object_sql)
        con.commit()
        data['id'] = cur.lastrowid
        response = data
        response['status'] = u'Добавлен новый объект учета'
    except Exception, e:
        response['status'] = u'Объект учета не добавлен. Причина: {e}'.format(e=e)
    return response

def update_object(objID, data, user_id=None):
    object_sql = u'''
    UPDATE objects
    SET 
        obj_desc='{obj_desc}'
    WHERE id={id} AND user_id={user_id}
    '''.format(
            obj_desc=data['obj_desc'],
            user_id=user_id,
            id=objID)

    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(object_sql)
        con.commit()
        response['status'] = u'Сохранено'
    except Exception, e:
        response['status'] = u'Не сохранено. Причина: {e}'.format(e=e)
    return response

def del_object(id, user_id=None):
    object_sql = u'''
    DELETE FROM objects
    WHERE id={id} AND user_id={user_id}
    '''.format(id=id, user_id=user_id)
    response = {'status': u'Неопределено'}
    try:
        cur, con = get_db()
        cur.execute(object_sql)
        con.commit()
        response['status'] = u'Удален объект учета'
    except Exception, e:
        response['status'] = u'Объект учета не удален. Причина: {e}'.format(e=e)
    return response