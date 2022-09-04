from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import errorcode
import  json
app = Flask(__name__)

try:
  cnx = mysql.connector.connect(user='root',
                                database='DBMS_PROJ')
  print("Success")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()


@app.route('/')
def home():
    cnxx = mysql.connector.connect(user='root',
                                  database='DBMS_PROJ')
    print("Success")
    cursor = cnxx.cursor()
    try:
        cursor.execute("INSERT INTO TEST VALUES(20)")
        cnx.commit()
        return "success"
    except mysql.connector.Error as err:
        print(err)
        return "error"

@app.route('/getAllClients')
def clients():
    cnxx = mysql.connector.connect(user='root',
                                   database='DBMS_PROJ')
    cursor = cnxx.cursor();
    tempDict={
        "ms":'',
        "gst_num":'',
        "locality":'',
        "city":'',
        "state":'',
        "pincode":'',
        "acc_num":''
    }
    try:
        cursor.execute("SELECT * FROM CLIENT")
        result=cursor.fetchall();
        data=[]
        for x in result:
            #print(x)
            tempDict["ms"]=x[0]
            tempDict["gst_num"]=x[1]
            tempDict["locality"]=x[2]
            tempDict["city"]=x[3]
            tempDict["state"]=x[4]
            tempDict["pincode"]=x[5]
            tempDict["acc_num"]=x[6]
            data.append(tempDict)

        final = json.dumps(data, indent=2)
        print(final)
        return data;
    except mysql.connector.Error as err:
        print(err)
        return "error"



if __name__ == "__main__":
    app.run(debug=True)