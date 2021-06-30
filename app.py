from flask import Flask
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
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


@app.route('/gettestdata/<mastertype>/<myname>/<getwratio>', methods = ['GET'] )
def gettestdata(mastertype,myname,getwratio=0):
    mylimit=50
    
    ##df['myindex'] = np.arange(1,len(df)+1)
    ##df['WRatio'] = 0
    strOptions = myname
    getwratio = int(getwratio)
    if strOptions=="" or len(strOptions)<=2:
            strOptions="zzzzz"
    if getwratio==0:
        getwratio=80
    mylist=[]
    mylist.append('test')
    mylist.append('test2')
    mylist.append('testing')
    
    ##return 'gettestdata1'
    ##myoutput = process.extractBests(strOptions, mylist, scorer=fuzz.WRatio,score_cutoff=getwratio,limit=mylimit)
    myoutput=[] 
    myoutput.append('test',80)
    myoutput.append('testing',90)

    myfound = pd.DataFrame(myoutput)
    return Response(myfound.to_json(orient="records"), mimetype='application/json')
    '''

