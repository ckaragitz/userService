from flask import Flask, request, jsonify, make_response
import os
import json
import random 
import string 
import psycopg2

app = Flask(__name__)

@app.route('/api/user/create', methods=['POST'])
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
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    phone = data.get("phone")
    age = data.get("age")
    gender = data.get("gender")
    location = data.get("location")
    timezone = data.get("timezone")

    print('\n')
    print(data)
    print(email)
    # Need to handle for registration questions/preferences #

    # Insertion operations
    cur.execute('INSERT INTO "user" (user_id, email, username, password, first_name, last_name, phone, age, \
         gender, location, timezone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (user_id, email, username, password, first_name, last_name, phone, age, gender, location, timezone))
    conn.commit()
    cur.close()

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/api/user/delete/<user_id>', methods=['POST'])
def delete_user(user_id):
   
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    # Deletion operations
    cur.execute("""DELETE FROM "user" WHERE "user_id" = '%s';""" % (user_id))
    conn.commit()
    cur.close()

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/api/user/<user_id>', methods=['GET'])
def search_user(user_id):
   
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    # Deletion operations
    cur.execute("""SELECT user_id, email, username, password, first_name, last_name, phone, age, \
         gender, location, timezone FROM "user" WHERE "user_id" = '%s';""" % (user_id))
    rows = cur.fetchall()
    cur.close()

    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
