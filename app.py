from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from models import ToDo

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

app = Flask(__name__)

app.config.from_object(os.environ["APP_SETTINGS"])

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
from database import db

db.init_app(app)

migrate = Migrate(app, db)


@app.route("/add", methods=["POST"])
def add():
    todo = request.form["todo"]
    new_todo = ToDo(
        todo=todo,
        params="{'test':'test'}",
    )
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/")
def index():
    todos = ToDo.query.all()
    return render_template("index.html", todos=todos)


if __name__ == "__main__":
    app.run()
