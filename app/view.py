from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user={'nickname':'dick'}
    return render_template("index.html",title='Dick',user=user)