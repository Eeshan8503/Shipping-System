from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import errorcode
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
    cnx = mysql.connector.connect(user='root',
                                  database='DBMS_PROJ')
    cursor = cnx.cursor()
    try:
        cursor.execute("INSERT INTO TEST VALUES(20)")
        cnx.commit()
        return "success"
    except mysql.connector.Error as err:
        print(err)
        return "error"


if __name__ == "__main__":
    app.run(debug=True)