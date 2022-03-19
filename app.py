from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def enregistrer():
    if request.method == 'POST':

        return render_template("validation.html")

    return render_template('form.html')

