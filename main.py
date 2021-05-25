from flask import Flask,render_template,request
import mysql.connector

app=Flask(__name__)
conn=mysql.connector.connect(host="remotemysql.com",user="84Mk5QDptt",password="z7IQSvfI6g",database="84Mk5QDptt")
cursor=conn.cursor()

@app.route('/')
def login():
    return render_template('login.html')
@app.route('/register')
def about():
    return render_template('registration.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM 'users' WHERE 'email' LIKE '{}' AND 'password' LIKE '{}' """
                   .format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        return render_template('home.html')
    else:
        return render_template('login.html')


if __name__=="__main__":
    app.run(debug=True)