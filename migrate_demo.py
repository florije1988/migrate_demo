# -*- coding: utf-8 -*-
__author__ = 'florije'

import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from sqlalchemy.sql.expression import false
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:903326@localhost:3306/migrate_demo'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    age = db.Column(db.Integer, server_default="0", nullable=True)
    record = db.Column(db.Integer, server_default=text("100"), nullable=False)
    gender = db.Column(db.Boolean, server_default=sa.sql.expression.false(), nullable=False)


@manager.command
def get_users():
    user_list = User.query.all()
    for user in user_list:
        print type(user.id), type(user.name), type(user.age), type(user.record)


if __name__ == '__main__':
    manager.run()
