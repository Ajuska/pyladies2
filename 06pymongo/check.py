#!/usr/bin/env python
from __future__ import print_function

# python version
import sys
if sys.version_info < (3,0):
	print("Python 3 is required")
	exit()

# venv
import os
venv = os.getenv('VIRTUAL_ENV')
if venv is None:
	print('Virtual environment is not detected')
	print('Use: python -m venv venv')
	print('     source venv/bin/activate')
	exit()

# pip
import pip
pip_version = pip.__version__.split('.')
if int(pip_version[0]) < 10:
	print('Python module pip version 10.x or newer is required')
	print('Use: python -m pip install --upgrade pip')
	exit()

# pymongo
try:
	import pymongo
except ModuleNotFoundError:
	print('Python module pymongo is not present')
	print('Use: python -m pip install pymongo')
	exit()

# faker
try:
	import faker
except ModuleNotFoundError:
	print('Python module faker is not present')
	print('Use: python -m pip install faker')
	exit()

# flask
try:
	import flask
except ModuleNotFoundError:
	print('Python module flask is not present')
	print('Use: python -m pip install flask')
	exit()

# flask-pymongo
try:
	import flask_pymongo
except ModuleNotFoundError:
	print('Python module flask-pymongo is not present')
	print('Use: python -m pip install flask-pymongo')
	exit()

# connection check
#try:
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
client = MongoClient(connectTimeoutMS=100, serverSelectionTimeoutMS=100)
try:
	client.admin.command('ismaster')
except ConnectionFailure:
	print("MongoDB server is not running")
	exit()

print("OK")
