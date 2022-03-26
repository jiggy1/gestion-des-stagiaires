import os

import psycopg2
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="manager_db",
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"]
    )
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM stagiaires;')
    stagiaires = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', stagiaires=stagiaires)


@app.route('/enregistrement', methods=['GET', 'POST'])
def enregistrement():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        departement = request.form['departement']
        genre = request.form['genre']
        conn = get_db_connection()
        cur = conn.cursor()
        error = None

        if not nom:
            error = 'Remplissez le nom.'

        elif not prenom:
            error = 'Remplissez le prénom.'

        if error is None:
            try:
                cur.execute('INSERT INTO stagiaires (nom, prenom, departement, genre)'
                            'VALUES (%s, %s, %s, %s)',
                            (nom, prenom, departement, genre)
                            )

                conn.commit()
            except psycopg2.IntegrityError as err:
                print(err)
                error = 'Ces informations ont deja été renseigné.'
        return render_template("validation.html")

    return render_template('enregistrement.html')

