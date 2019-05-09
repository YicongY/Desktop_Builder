import pymysql
import DateTime
import datetime
import math
import sys
import time
import heapq
import metapy
import pytoml
import json

class basic_budget():
    def __init__(self):
        self.budget = {}
        self.budget['cpu'] = 0.3
        self.budget['gpu'] = 0.29
        self.budget['board'] = 0.1
        self.budget['ram'] = 0.1
        self.budget['hdd'] = 0.08
        self.budget['psu'] = 0.07
        self.budget['case'] = 0.06

class gaming_budget():
    def __init__(self):
        self.budget = {}
        self.budget['cpu'] = 0.17
        self.budget['gpu'] = 0.30
        self.budget['board'] = 0.1
        self.budget['ram'] = 0.15
        self.budget['hdd'] = 0.14
        self.budget['psu'] = 0.1
        self.budget['case'] = 0.08

class working_budget():
    def __init__(self):
        self.budget = {}
        self.budget['cpu'] = 0.3
        self.budget['gpu'] = 0.2
        self.budget['board'] = 0.1
        self.budget['ram'] = 0.15
        self.budget['hdd'] = 0.14
        self.budget['psu'] = 0.1
        self.budget['case'] = 0.06

