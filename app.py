from flask import Flask, render_template, redirect, flash, session, request, jsonify
import json, datetime
app = Flask(__name__)
app.secret_key='Cynergy'
@app.route('/')
def base():
    return redirect('/index')

@app.route('/index')
def index():
  datafile=open("./tmp/data.json","r")
  data=json.loads(datafile.read())
  print(data)
  return render_template(f'index.html',data=data)

@app.route('/pqrcode/<name>')
def pqrcode(name):
  datafile=open("./tmp/data.json","r")
  apdata=json.loads(datafile.read())["data"]
  pdata=[ temp for temp in apdata if temp['id']==name ][0]
  print(pdata)
  return render_template(f'pqrcode.html',name=name,pdata=pdata)


@app.route('/scan',methods=['GET', 'POST'])
def scan():
  datafile=open("./tmp/data.json","r")
  data=json.loads(datafile.read())
  if(request.method=='GET'):
    return render_template(f'scan.html',data=data)
  elif(request.method=='POST'):
    if(request.form["status"]=="reset"):
      return jsonify(data=data)
    id=request.form["id"]
    for val in data["data"]:
      if val["id"]==id:
        if(request.form["status"]=="arrived"):
          if(val["arrive"]=="No"):
            now=datetime.datetime.now()
            time = now.strftime("%H:%M:%S")
            val["arrival_time"]=time
          val["arrive"]="Yes"
          val["present"]="Yes"
        elif(request.form["status"]=="leaving"):
          val["present"]="No"
        break
    restructured_json = json.dumps(data, indent=4, ensure_ascii=False)
    with open("./tmp/data.json", "w") as outfile:
      outfile.write(restructured_json)
    
    datafile=open("./tmp/data.json","r")
    data=json.loads(datafile.read())

    print(request.form["id"])
    print(data)
    return jsonify(data=data)

@app.route('/aqrcode')
def aqrcode():
  datafile=open("./tmp/data.json","r")
  data=json.loads(datafile.read())
  print(data)
  return render_template(f'aqrcode.html',data=data)

if __name__ == "__main__":
  app.run(debug=True)