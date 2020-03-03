from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
import yaml

app = Flask(__name__)


@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/login')
def register():
    return render_template('login.html')

@app.route('/send',methods=['GET','POST'])
def send():
    if request.method=='POST':
        Email=request.form['Email']
        Password=request.form['password']
    return render_template('login.html')    

app.run(host = "localhost", debug = True)