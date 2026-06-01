from flask import Flask, render_template, request
import os 
import sqlite3 
app=Flask(__name__) 
BASE_DIR=os.path.dirname(os.path.abspath(__file__)) 
db_path = os.path.join(BASE_DIR, "studentregistration.db") 
@app.route('/',methods=['GET','POST']) 
def home(): 
  if request.method=="POST":
    username=request.form['username']
    age=request.form['age']
    email=request.form['email']
    password=request.form['password']
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS studentregistration(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    email TEXT,
    password TEXT)""")
    cursor.execute("INSERT INTO studentregistration(name,age,email,password) VALUES(?,?,?,?)",(username,age,email,password))
    conn.commit()
    print(os.path.abspath("studentregistration.db"))
    conn.close()
    return render_template('home.html',username=username,age=age,email=email,password=password) 
  return render_template('home.html')
@app.route('/about') 
def about():
 return render_template('about.html')
@app.route('/contact') 
def contact(): 
  return render_template('contact.html',phone="998506881",city="USA")

@app.route("/students")
def students():
    conn=sqlite3.connect(db_path)
    cursor=conn.cursor()
    cursor.execute("select * from studentregistration")
    data=cursor.fetchall()
    conn.close()
    return render_template("students.html",students=data)

@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
  conn=sqlite3.connect(db_path)
  cursor=conn.cursor()
  if request.method=="POST":
    username=request.form["username"]
    age=request.form["age"]
    email=request.form["email"]
    password=request.form["password"]
    cursor.execute("update studentregistration set name=?,age=?,email=?,password=? where id=?",(username,age,email,password,id))
    conn.commit()
    conn.close()
    return "update successfully"
  cursor.execute("select * from studentregistration where id=?",(id,))
  student=cursor.fetchone()
  conn.close()
  return render_template("update.html",student=student)

@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id):
  conn=sqlite3.connect(db_path)
  cursor=conn.cursor()
  if request.method=="POST":
    cursor.execute("delete from studentregistration where id=?",(id,))
    conn.commit()
    conn.close()
    return "delete successfully"
  cursor.execute("select * from studentregistration where id=?",(id,))
  student=cursor.fetchone()
  conn.close()
  return render_template("delete.html",student=student)
app.run(debug=True)
