import os
import psycopg2
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='postgresql',
                            database='dvdrental',
                            user="admin",
                            password="adminadmin")
    print(conn)
    print("success")
    return conn


@app.route('/film', methods=['GET'])
def film_get():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM film;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return books


@app.route('/film/<int:filmID>', methods=['GET'])
def one_film(filmID):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM film WHERE film_id = {filmID}')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return books


@app.route('/film', methods=['POST'])
def film_post():
    data = request.json
    con = get_db_connection()
    cur = con.cursor()
    name = data.get('name')
    desc = data.get('description')
    cur.execute(f"INSERT INTO film (title, description, language_id) VALUES (%s, %s, 1)", (name, desc))
    con.commit()
    cur.close()
    con.close()
    return "success"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="9000")
