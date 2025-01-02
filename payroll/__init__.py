from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///payroll.db"
db = SQLAlchemy(app)

from payroll import models
from payroll import routes