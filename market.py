from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world(): 
    return '<h1>Hey</h1>'

@app.route('/taxes/<society>')
def compute_tax(society) :
    return f'Here we gonna implements tax computation for {society}'