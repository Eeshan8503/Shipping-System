from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import errorcode
import  json
from Utils.decorators import *
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
@async_caller
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
    # try:
    #     cursor.execute("SELECT * FROM CLIENT")
    #     result=cursor.fetchall();
    #     data=[]
    #     for x in result:
    #         #print(x)
    #         tempDict["ms"]=x[0]
    #         tempDict["gst_num"]=x[1]
    #         tempDict["locality"]=x[2]
    #         tempDict["city"]=x[3]
    #         tempDict["state"]=x[4]
    #         tempDict["pincode"]=x[5]
    #         tempDict["acc_num"]=x[6]
    #         data.append(tempDict)
    #
    #     final = json.dumps(data, indent=2)
    #     print(final)
    #     return data;
    # except mysql.connector.Error as err:
    #     print(err)
    #     return "error"
    cursor.execute("SELECT * FROM CLIENT")
    result = cursor.fetchall();
    data = []
    for x in result:
        # print(x)
        tempDict["ms"] = x[0]
        tempDict["gst_num"] = x[1]
        tempDict["locality"] = x[2]
        tempDict["city"] = x[3]
        tempDict["state"] = x[4]
        tempDict["pincode"] = x[5]
        tempDict["acc_num"] = x[6]
        data.append(tempDict)

    final = json.dumps(data, indent=2)
    print(final)
    return data;


@app.route('/addInvoice')
def add_invoice():
    cnxx = mysql.connector.connect(user='root',
                                   database='DBMS_PROJ')
    cursor = cnxx.cursor();
    data = request.json
    print(data['destination'])
    try:
        cursor.execute(
            f"INSERT INTO CONTAINER (CONTAINER_NUM,DESTINATION,VESSEL) VALUES('{data['container_num']}','{data['destination']}','{data['vessel']}');")
        cursor.execute(f"INSERT INTO SHIPPING_AGENT(INVOICE_NUM,MS)VALUES('{data['invoice_num']}','{data['ms']}')")
        cursor.execute(
            f"INSERT INTO CHARGES (AMOUNT,CHARGE_TYPE,CONTAINER_NUM,CURRENCY,INVOICE_NUM,QUANTITY,RATE) VALUES('{data['amount']}','{data['charge_type']}','{data['container_num']}','{data['currency']}','{data['invoice_num']}','{data['quantity']}','{data['rate']}')")

        cnxx.commit()
    except Exception as err:
        print(err)
        return err

    return data



if __name__ == "__main__":
    app.run(debug=True)