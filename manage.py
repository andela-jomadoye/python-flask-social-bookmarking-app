#! /usr/bin/env python
from HelloWorld import app, db
from flask.ext.script import Manager, prompt_bool
from HelloWorld.models import User

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="ww", email="ww@email.com"))
    db.session.add(User(username="ee", email="ee@email.com"))
    db.session.commit()
    print('============================')
    print('DB initialized')
    print('============================')


@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to drop this DB"
    ):
        db.drop_all()
        print('Database deleted')

if __name__ == '__main__':
    manager.run()
