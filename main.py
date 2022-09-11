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
            print(x)
            tempDict["ms"]=x[0]
            tempDict["invoice_num"]=x[1]
            # if x[2]!=None:
            #     tempDict["date"]=x[2]
            tempDict["container_num"]=x[3]
            tempDict["destination"]=x[4]
            tempDict["amount"]=x[5]
            data.append(tempDict)

        final = json.dumps(data, indent=2)
        print("here")
        return jsonify(data);
    except mysql.connector.Error as err:
        print(err)
        return jsonify({"error": err})


@app.route('/addInvoice' ,  methods=['GET', 'POST'])
def add_invoice():
    cnxx = mysql.connector.connect(user='root',
                                   database='DBMS_PROJ')
    cursor = cnxx.cursor();
    data = request.json
    print(data)
    response = {
        "message": ""
    }
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
    except mysql.connector.Error as err:
        print(err.msg)
        response["message"]=err.msg
        return response

@app.route('/admin')
def admin():
    cnxx = mysql.connector.connect(user='root',
                                   database='DBMS_PROJ')
    cursor = cnxx.cursor();
    data = request.json;
    lst = data['filter']
    projections=""
    for i in lst:
        i=i.upper()
        projections=projections+i+" ";
    space=projections.count(" ");
    # print(space)
    projections=projections.replace(' ',',',space-1)
    table="";
    lst2=data['table'];
    for i in lst2:
        i=i.upper()
        table=table+i+" ";
    space = table.count(" ");
    table=table.replace(' ',',',space-1);
    query=f"SELECT {projections} FROM {table}"
    # print(query)
    cursor.execute(query)
    result = cursor.fetchall();
    # print(result)
    # print(lst)
    result.append(query)
    print(result[len(result)-1])
    return (result)

@app.route('/createView')
def createView():
    cnxx = mysql.connector.connect(user='root',
                                   database='DBMS_PROJ')
    cursor = cnxx.cursor();
    data = request.json;
    name=data['name'];
    query=data['query']
    try:
        cursor.execute(f"Create VIEW {name} as {query}");
        cnxx.commit();
        response={
            "message":"View created"
        }
        return response;
    except mysql.connector.Error as err:
        print(err.msg)
        response["message"]=err.msg
        return response
@app.route('/runQuery')
def run_query():
    cnxx = mysql.connector.connect(user='root',
                                   database='DBMS_PROJ')
    cursor = cnxx.cursor();
    query=request.json['query'];
    response = {
        "message":""
    }
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        cnxx.commit()
        return result


    except mysql.connector.Error as err:
        print(err.msg)
        response["message"]=err.msg
        return response
@app.route('/search')
def search():
    cnxx = mysql.connector.connect(user='root',
                                   database='DBMS_PROJ')
    cursor = cnxx.cursor();
    data=request.json
    response = {
        "message": ""
    }
    query=f"SELECT * FROM {data['from']} WHERE {data['field']} = {data['equals']}"
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result

    except mysql.connector.Error as err:
        print(err.msg)
        response["message"]=err.msg
        return response

app.route('/stats')
def stats():

if __name__ == "__main__":
    app.run(debug=True)