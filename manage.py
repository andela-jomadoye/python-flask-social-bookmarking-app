#! /usr/bin/env python

from thermos import app, db
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    print('DB initialized')

@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to drop this DB"
    ):
        db.drop_all()
        priint('Database deleted')

if __name__ == '__main__':
    manager.run()
