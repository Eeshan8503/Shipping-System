from flask import Flask, render_template, request, jsonify
import mysql.connector
from mysql.connector import errorcode
import  json
from flask_cors import CORS, cross_origin
from Utils.decorators import *
app = Flask(__name__)
CORS(app)
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

    }
    try:
        cursor.execute("SELECT CLIENT.MS,SHIPPING_AGENT.INVOICE_NUM,DATE,CONTAINER.CONTAINER_NUM,DESTINATION,AMOUNT FROM CLIENT,CHARGES,CONTAINER,SHIPPING_AGENT;")
        result=cursor.fetchall();
        data=[]
        for x in result:
            #print(x)
            tempDict["ms"]=x[0]
            tempDict["invoice_num"]=x[1]
            tempDict["date"]=x[2]
            tempDict["container_num"]=x[3]
            tempDict["destination"]=x[4]
            tempDict["amount"]=x[5]
            data.append(tempDict)

        final = json.dumps(data, indent=2)
        print(final)
        return data;
    except mysql.connector.Error as err:
        print(err)
        return "error"


@app.route('/addInvoice' ,  methods=['GET', 'POST'])
def add_invoice():
    cnxx = mysql.connector.connect(user='root',
                                   database='DBMS_PROJ')
    cursor = cnxx.cursor();
    data = request.json
    print(data)
    try:
        print("TRY 1")
        cursor.execute(f"INSERT INTO CLIENT(ACC_NUM,CITY,GST_NUM,LOCALITY,MS,PINCODE,STATE) VALUES('{data['acc_num']}','{data['city']}','{data['gst_num']}','{data['locality']}','{data['ms']}','{data['pincode']}','{data['state']}');")
        cursor.execute(
            f"INSERT INTO CONTAINER (CONTAINER_NUM,DESTINATION,VESSEL) VALUES('{data['container_num']}','{data['destination']}','{data['vessel']}');")
        cursor.execute(f"INSERT INTO SHIPPING_AGENT(INVOICE_NUM,MS,DATE)VALUES('{data['invoice_num']}','{data['ms']}',NOW())")
        cursor.execute(
            f"INSERT INTO CHARGES (AMOUNT,CHARGE_TYPE,CONTAINER_NUM,CURRENCY,INVOICE_NUM,QUANTITY,RATE) VALUES('{data['amount']}','{data['charge_type']}','{data['container_num']}','{data['currency']}','{data['invoice_num']}','{data['quantity']}','{data['rate']}')")
        print("tr33")
        cnxx.commit()
        return data
    except Exception as err:
        print(err)
        print("heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        return err





if __name__ == "__main__":
    app.run(debug=True)