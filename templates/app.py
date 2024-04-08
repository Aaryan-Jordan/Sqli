
from flask import Flask, render_template, request
import sqlite3
from passlib.hash import bcrypt

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    u = request.form['username']
    p = request.form['password']

    conn = sqlite3.connect('l3.db')
    c = conn.cursor()

    #query = "SELECT * FROM cred WHERE username='red' OR '1'='1'"
    query = "SELECT * FROM cred WHERE username='" + u + "'AND password = '" + p + "'";
    print ("q=",query)
    c.execute(query)
    result = c.fetchone()

    if result :
        return render_template('landing.html')
    else:
        return 'Invalid credentials'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
