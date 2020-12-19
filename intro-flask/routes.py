from flask import Flask, request, url_for, redirect, abort, render_template

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jonulo321",
    database="prueba"
)

cursor = mydb.cursor(dictionary=True)

app = Flask(__name__)

# Get TABLE DATA (structure/for info)
cursor.execute('show create table Usuario')
result = cursor.fetchall()
print(result)

# Decorator:
@app.route('/')
def index():
    return 'hola mundo'

# Example enabling METHODS and passing data in the URL
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def another(post_id):
    return 'el id del post es: ' + post_id

# Templates, and extending them
@app.route('/landing', methods=['GET'])
def templatesFunction():
    return render_template('home.html', message="Hello World")

# GET Data from BD (create BD connection and cursor)
@app.route('/datadb', methods=['POST', 'GET'])
def getData():
    cursor.execute('select * from Usuario')
    users = cursor.fetchall()

    return render_template('dataFromDB.html', users=users)

# ADD Data to DB
@app.route('/addUser', methods=['POST', 'GET'])
def addNewUser():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        age = request.form['age']

        sql = "insert into Usuario (email, username, edad) values (%s, %s, %s)"
        values = (username, email, age)
        cursor.execute(sql, values)
        mydb.commit()

        return redirect(url_for('getData'))

    return render_template('addUser.html')
