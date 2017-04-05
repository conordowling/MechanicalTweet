#!/bin/bash
mongod --logpath log/mongodb.log
export FLASK_APP=server.py
python -m flask run
