from flask import Flask,render_template, request

import forms
import math

app=Flask(__name__)

@app.route("/OperasBas")
def operas():
    return render_template("OperasBas.html")

@app.route("/resultado",methods=["GET","POST"])
def resul():
     if request.method=="POST":
        radio=request.form.get("ope")
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        if radio=="suma":
            return"La suma de este {} + {} = {}".format(num1,num2,str(int(num1)+int(num2)))
        elif radio=="resta":
            return"La resta de este {} - {} = {}".format(num1,num2,str(int(num1)-int(num2)))
        elif radio=="multi":
            return"La multiplicacion de este {} x {} = {}".format(num1,num2,str(int(num1)*int(num2)))
        elif radio=="divi":
            return"La division de este {} / {} = {}".format(num1,num2,str(int(num1)/int(num2)))

@app.route("/prac",methods=['GET','POST'])
def prac():
    disp=""
    distancia1=""
    distancia2=""
    distancia3=""
    distancia4=""
    distancia_clase= forms.UserForm(request.form)
    if request.method=='POST':
        distancia1=distancia_clase.distancia1.data
        distancia2=distancia_clase.distancia2.data
        distancia3=distancia_clase.distancia3.data
        distancia4=distancia_clase.distancia4.data
        disp= math.sqrt((distancia3-distancia1)**2+(distancia4-distancia2)**2)
        
        print('dkd {}'.format(disp))
    
    return render_template("practica.html",form=distancia_clase,disp=disp, distancia1=distancia1, distancia2=distancia2, distancia3=distancia3, distancia4=distancia4)
    
        
if __name__=="__main__":
    app.run(debug=True)
        