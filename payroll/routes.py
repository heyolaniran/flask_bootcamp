from payroll import app, db
from flask import render_template


@app.cli.command('create_db')
def create_db():
    """Create the database and tables."""
    db.create_all()
    print("Database created!")

@app.cli.command('update_db')
def update_db(): 
    """ Update the Database and tables with latest changes."""
    db.update_all()
    print("Database updated!")

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