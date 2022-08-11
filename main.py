from flask import Flask, render_template, request
from flask_mysql_connector import MySQL
#
app = Flask(__name__)
#
# app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''

mysql = MySQL(app)
@app.route('/')
def home():
    # cur = mysql.new_cursor(dictionary=True)
    # cur.execute('CREATE DATABASE DBMS_PROJ')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)