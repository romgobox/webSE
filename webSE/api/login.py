# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for, flash, g
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUserMixin,
                            confirm_login, fresh_login_required)
from webSE import app
from webSE.api.model.login import get_user_by_id, get_user_by_name

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.setup_app(app)

@login_manager.user_loader
def user_loader(id):
    return get_user_by_id(int(id))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = ''
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_name(username)
        if user:
            if user.verify_password(password):
                remember = False
                login_user(user, remember=remember)
                g.user = current_user.id
                return redirect(request.args.get('next') or url_for("webamr_index"))
            else:
                error = u'Неверный пароль'
        else:
            error=u'Пользователь не найден'
    return render_template("login.html", error=error)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("login"))

@app.before_request
def load_user():
    if current_user.is_authenticated:
        g.user = current_user.id
    else:
        g.user = None
