# -*- coding: utf-8 -*-
from passlib.apps import custom_app_context as pwd_context
from flask.ext.login import UserMixin
from webSE.api.model import get_db

class User(UserMixin):
    def __init__(self, username, password, id, is_active=True):
        self.username = username
        self.password = password
        self.id = id
        self.is_active = is_active

    def is_active(self):
        return self.is_active

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

def get_user_by_id(id):
    user_sql = '''
    SELECT 
        u.id,
        u.username,
        u.password,
        u.name,
        u.user_token,
        u.organisation_id,
        u.role_id,
        u.is_active
    FROM 
        users u
    WHERE id={id}
    '''.format(id=id)

    cur, con = get_db()
    cur.execute(user_sql)
    user = cur.fetchone()
    if user:
        user = User(username=user['username'], 
                    password=user['password'], 
                    id=user['id'], 
                    is_active=user['is_active'])
    else:
        user = None
    return user

def get_user_by_name(username):
    user_sql = '''
    SELECT 
        u.id,
        u.username,
        u.password,
        u.name,
        u.user_token,
        u.organisation_id,
        u.role_id,
        u.is_active
    FROM 
        users u
    WHERE username='{username}'
    '''.format(username=username)

    cur, con = get_db()
    cur.execute(user_sql)
    user = cur.fetchone()
    if user:
        user = User(username=user['username'], 
                    password=user['password'], 
                    id=user['id'], 
                    is_active=user['is_active'])
    else:
        user = None
    return user