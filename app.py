from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/biblioteca")
def biblioteca():
    return render_template("biblioteca.html")

@app.route("/biblioteca/cadastra_pessoa")
def bibl_cadpessoa():
    return render_template("bibl_cadpessoa.html")


if __name__ == '__main__':
    app.run(debug=True)