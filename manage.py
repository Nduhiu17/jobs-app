#!/usr/bin/env bash

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()
