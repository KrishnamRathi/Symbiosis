from flask import Flask, render_template,request
from flask_mysqldb import MySQL
from flask_bootstrap import Bootstrap
import yaml

app = Flask(__name__)

#Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_db']

mysql=MySQL(app)

@app.route('/farmers') 
def users():
    cur=mysql.connection.cursor()
    resultValue= cur.execute("SELECT * FROM farmer")
    return render_template('index.html')


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
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO farmers(email,password) VALUES(%s,%s)",(email,password))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('login.html')    

app.run(host = "localhost", debug = True)