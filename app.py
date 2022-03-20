from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/enregistrement', methods=['GET', 'POST'])
def enregistrement():
    if request.method == 'POST':

        return render_template("validation.html")

    return render_template('enregistrement.html')

