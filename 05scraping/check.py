#https://gist.github.com/yaplik/f1f76666d0e21ce8b187adbaac31c5cc
#IF ERROR WHEN INSTALLING SCRAPY DO
#SUDO DNG GROUPINSTLL "DEVELOPMENT TOOLS" || and || "sudo dnf install python3-devel python-devel -y"

#PREREQUISITIES - VENV, UPGRADE PIP, SCRAPY, FLASK, THEN CHECK IT WITH THIS SCRIPT

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

# flask
try:
	import flask
except ModuleNotFoundError:
	print('Python module flask is not present')
	print('Use: python -m pip install flask')
	exit()

# scrapy
try:
	import scrapy
except ModuleNotFoundError:
	print('Python module scrapy is not present')
	print('Use: python -m pip install scrapy')
	exit()

print("OK")
