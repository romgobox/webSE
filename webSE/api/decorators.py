# -*- coding: utf-8 -*-

from functools import wraps
from flask import redirect, url_for, g

def user_required(f):
    ''' В методах API проверяем авторизацию пользователя,
        если не авторизован отправляем на страницу логина
    '''
    @wraps(f)
    def decorator(*args, **kwargs):
        if not g.user:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorator