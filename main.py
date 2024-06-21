from flask import Flask
from flask_bootstrap import Bootstrap5

app=Flask(__name__)
app.config['SECRET_KEY'] = 'ftyfguhijijokopkopkpok'
Bootstrap5(app=app)







@app.route('/')
def home():
    pass