from flask import Flask
from fuzzywuzzy import fuzz
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
