from flask import Flask, request, jsonify, make_response
import os
import random 
import string 
import psycopg2

app = Flask(__name__)

@app.route('/api/user/create')
def create_user():
   
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    
    # User ID Generator
    user_id = ''.join([random.choice(string.ascii_letters 
            + string.digits) for n in range(6)]) 

    # Receive POST body and parse for values
    data = request.json
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")
    first_name = data.get("first")
    last_name = data.get("last")
    phone = data.get("phone")
    age = data.get("age")
    gender = data.get("gender")
    location = data.get("location")
    timezone = data.get("timezone")
    # Need to handle for registration questions/preferences #

    # Insertion operations
    cur.execute('INSERT INTO %s (user_id, email, username, password, first_name, last_name, phone, age, \
         gender, location, timezone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (user_id, email, username, password, first_name, last_name, phone, age, gender, location, timezone))
    conn.commit()
    cur.close()


@app.route('/api/user/delete')
def delete_user():
   pass