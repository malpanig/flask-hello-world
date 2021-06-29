from flask import *
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

@app.route('/getdata/<mastertype>/<myname>/<getwratio>', methods = ['GET'] )
def getdata(mastertype,myname,getwratio=0):
    mylimit=50
    if mastertype in ['client','agency','brand','program','bookingref']:
        if mastertype=="client":
            sqlstring="select 'client' mcategory,  clientname mastername from clientmaster"
        if mastertype=="agency":
            sqlstring="select 'agency' mcategory,  agencyname mastername from agencymaster"
        if mastertype=="brand":
            sqlstring="select 'brand' mcategory,  brandname mastername from brandmaster"
        if mastertype=="program":
            sqlstring="select 'program' mcategory,  programname mastername from programmaster"
        if mastertype=="rmsprogram":
            sqlstring="select 'rmsprogram' mcategory,  programname mastername from programgroup"
        if mastertype=="bookingref":
            sqlstring="select 'booking' mcategory, bookingreferencenumber mastername from bookingmaster where "
            sqlstring=sqlstring+"channelcode='zazee00001' and locationcode='zazee00001' and bookingdate >='1-oct-2020'"
            mylimit=10
        print(sqlstring)        
        connection = pypyodbc.connect('Driver={SQL Server};Server=172.16.4.38;Database=BMS;uid=bms_user;pwd=bms@zeel')
        SQL_Query = pd.read_sql_query(sqlstring,connection)
        
    if mastertype in ['employee']:
        connection = pypyodbc.connect('Driver={SQL Server};Server=172.16.4.38;Database=NEWCMS;uid=Essel_Connect;pwd=Essel@onnect')
        SQL_Query = pd.read_sql_query('''select  'employee' mcategory, employeename mastername from sapemployeemaster where status='3' ''',connection)
     
    df = pd.DataFrame(SQL_Query)
        
    ##df['myindex'] = np.arange(1,len(df)+1)
    ##df['WRatio'] = 0
    strOptions = myname
    getwratio = int(getwratio)
    if strOptions=="" or len(strOptions)<=2:
            strOptions="zzzzz"
    if getwratio==0:
        getwratio=80
        
    mylist=df['mastername'].astype(str).values.tolist()  
    
    ##print(mylist)
    myoutput = process.extractBests(strOptions, mylist, scorer=fuzz.WRatio,score_cutoff=getwratio,limit=mylimit)
    ##print(myoutput)
    
    '''
    for index , row in df.iterrows():
            
          myempname = str(row['mastername'])
          myindex = row['myindex']
        
          wRatio = fuzz.WRatio(myempname,strOptions)
          df.at[myindex-1,'WRatio'] = wRatio
            
    ##myfound = df[(df['WRatio']>=getwratio)]
    '''
    myfound = pd.DataFrame(myoutput)
    
    
    ##cursor.close()
    connection.close()
    ##tb = [myfound.to_html(classes='fl-table')]
    ##return render_template('view.html',tables=tb,titles = "titles1", user_image="gst")
    ##return Response(myfound[{'mcategory','mastername','WRatio'}].to_json(orient="records"), mimetype='application/json')
    return Response(myfound.to_json(orient="records"), mimetype='application/json')
    


@app.route('/getbookingdata/<mastertype>/<locationcode>/<channelcode>/<monthcode>/<myname>/<getwratio>', methods = ['GET'] )
def getbookingdata(mastertype,locationcode,channelcode,monthcode,myname,getwratio=0):
    mylimit=50
    if mastertype in ['bookingref']:
        if mastertype=="bookingref":
            sqlstring="select 'booking' mcategory, bookingreferencenumber mastername from bookingmaster where "
            sqlstring=sqlstring+"channelcode='"+ channelcode+ "' and locationcode= '"+ locationcode + "' " 
            sqlstring = sqlstring+ "and left ( bookingnumber , 4 ) = '" + monthcode + "'"
            mylimit=10
        print(sqlstring)        
        connection = pypyodbc.connect('Driver={SQL Server};Server=172.16.4.38;Database=BMS;uid=bms_user;pwd=bms@zeel')
        SQL_Query = pd.read_sql_query(sqlstring,connection)
        
    df = pd.DataFrame(SQL_Query)
    
    ##df['myindex'] = np.arange(1,len(df)+1)
    ##df['WRatio'] = 0
    strOptions = myname
    getwratio = int(getwratio)
    if strOptions=="" or len(strOptions)<=2:
            strOptions="zzzzz"
    if getwratio==0:
        getwratio=80
        
    mylist=df['mastername'].astype(str).values.tolist()  
    
    ##print(mylist)
    myoutput = process.extractBests(strOptions, mylist, scorer=fuzz.WRatio,score_cutoff=getwratio,limit=mylimit)
    ##print(myoutput)
    
    '''
    for index , row in df.iterrows():
            
          myempname = str(row['mastername'])
          myindex = row['myindex']
        
          wRatio = fuzz.WRatio(myempname,strOptions)
          df.at[myindex-1,'WRatio'] = wRatio
            
    ##myfound = df[(df['WRatio']>=getwratio)]
    '''
    myfound = pd.DataFrame(myoutput)
    
    
    ##cursor.close()
    connection.close()
    ##tb = [myfound.to_html(classes='fl-table')]
    ##return render_template('view.html',tables=tb,titles = "titles1", user_image="gst")
    ##return Response(myfound[{'mcategory','mastername','WRatio'}].to_json(orient="records"), mimetype='application/json')
    return Response(myfound.to_json(orient="records"), mimetype='application/json')


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
        
    mylist=['test','test1','testing','tester'] 
    
    ##print(mylist)
    myoutput = process.extractBests(strOptions, mylist, scorer=fuzz.WRatio,score_cutoff=getwratio,limit=mylimit)
    ##print(myoutput)
    
    myfound = pd.DataFrame(myoutput)
    return Response(myfound.to_json(orient="records"), mimetype='application/json')


