from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///payroll.db"
db = SQLAlchemy(app)

class Payroll(db.Model): 
    id = db.Column(db.Integer(), primary_key=True)
    base_name = db.Column(db.String(255), nullable=False)
    base_url= db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())

    def __repr__(self): 
        return f'Payroll for {self.base_name}'

@app.cli.command('create_db')
def create_db():
    """Create the database and tables."""
    db.create_all()
    print("Database created!")

@app.route('/')
def home_page(): 
    return render_template('home.html', page_name="Home")

@app.route('/payroll')

def payroll_page(): 
    return render_template('payroll.html', page_name="Payroll")

"""@app.route('/taxes/<society>')
def compute_tax(society) :
    return f'Here we gonna implements tax computation for {society}'
"""