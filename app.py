from flask import Flask, render_template
import mysql.connector

app  = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kitchen"
)

mycursor = mydb.cursor(dictionary=True)

@app.route('/')
def index():
    mycursor.execute("SELECT * FROM Cabinet")
    cabinets = mycursor.fetchall()

    return render_template('index.html', cabinets=cabinets)

@app.route('/products/create')
def create_product():
    return render_template('add_product.html') 