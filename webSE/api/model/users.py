#! /usr/bin/python
# -*- coding: utf-8 -*-
import json
import datetime
from webSE.api.model import get_db

def get_user_info(user_id=None):
    user_sql = '''
    SELECT
        u.id,
        u.name,
        u.username,
        org.id org_id,
        org.name org_name,
        org.inn org_inn,
        org.desc org_desc,
        org.email org_email,
        org.contacts org_contacts,
        r.id role_id,
        r.name role_name,
        r.short_name role_short_name
    FROM users u
    LEFT JOIN organisations org ON u.organisation_id=org.id
    JOIN user_roles r ON u.role_id=r.id
    WHERE u.id={user_id};
    '''.format(user_id=user_id)

    cur, con = get_db()
    cur.execute(user_sql)
    user_result = dict(cur.fetchone())
    user = {
        'id': user_id,
        'name': user_result['name'],
        'username': user_result['username'],
        'role': {
            'id': user_result['role_id'],
            'name': user_result['role_name'],
            'short_name': user_result['role_short_name']
        },
        'organisation': {
            'id': user_result['org_id'],
            'name': user_result['org_name'],
            'inn': user_result['org_inn'],
            'desc': user_result['org_desc'],
            'email': user_result['org_email'],
            'contacts': user_result['org_contacts'],
        }
    }

    return user
