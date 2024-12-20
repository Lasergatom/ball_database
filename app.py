from flask import Flask, render_template, redirect, flash, session, request
import json, datetime
app = Flask(__name__)
app.secret_key='Cynergy'
@app.route('/')
def base():
    return redirect('/index')

@app.route('/index')
def index():
  datafile=open("data/data.json","r")
  data=json.loads(datafile.read())
  print(data)
  return render_template(f'index.html',data=data)

@app.route('/pqrcode/<name>')
def pqrcode(name):
  datafile=open("data/data.json","r")
  apdata=json.loads(datafile.read())["data"]
  pdata=[ temp for temp in apdata if temp['id']==name ][0]
  print(pdata)
  return render_template(f'pqrcode.html',name=name,pdata=pdata)


@app.route('/scan')
def scan():
  datafile=open("data/data.json","r")
  data=json.loads(datafile.read())
  print(data)
  return render_template(f'scan.html',data=data)

@app.route('/aqrcode')
def aqrcode():
  datafile=open("data/data.json","r")
  data=json.loads(datafile.read())
  print(data)
  return render_template(f'aqrcode.html',data=data)

if __name__ == "__main__":
  app.run(debug=True)