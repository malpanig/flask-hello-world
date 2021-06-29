from flask import Flask
from fuzzywuzzy import fuzz
import numpy as np
import pypyodbc
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/dashboard/<name>')
def dashboard(name):   
    return 'welcome %s' % name
