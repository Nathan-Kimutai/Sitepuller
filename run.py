#!/usr/bin/env python3
from flask_script import Manager,Shell
from app import create_app

#we should import db right now and make thins workd

app = create_app("default")
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
