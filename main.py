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
    
@app.route("/resistencia",methods=['GET','POST'])
def resistencia():
    color1=""
    color2=""
    color3=""
    tolerancia=""
    total =""
    maxim =""
    minm =""
    co1=''
    co2=''
    co3=''
    tol=''
    horale=''
    horale2=''
    horale3=''
    tole=''
    
    resistencia_clase =forms.Resis(request.form)
    if request.method=='POST':
        color1 = resistencia_clase.color1.data
        color2 = resistencia_clase.color2.data
        color3 = resistencia_clase.color3.data
        tolerancia = resistencia_clase.tolerancia.data
        total = int(str(color1) + str(color2)) * color3
        
          
            
        if color1 == 0:
            co1='Negro'
            horale='#565f5b'
        elif color1 == 1:
            co1 ='Cafe'
            horale='#a05b3d'
        elif color1 == 2:
            co1 ='Rojo'
            horale='#ea1e1b'
        elif color1 == 3:
            co1 ='Naranja'
            horale='#f2863e'
        elif color1 == 4:
            co1 ='Amarillo'
            horale='#f2e23e'
        elif color1 == 5:
            co1 ='Verde'
            horale='#bbe231'
        elif color1 == 6:
            co1 ='Azul'
            horale='#71a4e2'
        elif color1 == 7:
            co1 ='Violeta'
            horale='#a571e2'
        elif color1 == 8:
            co1 ='Gris'
            horale='#dbd5e2'
        else:
            co1 ='Blanco'
            horale='#fefbfb'
            
        if color2 == 0:
            co2='Negro'
            horale2='#565f5b'
        elif color2 == 1:
            co2 ='Cafe'
            horale2='#a05b3d'
        elif color2 == 2:
            co2 ='Rojo'
            horale2='#ea1e1b'
        elif color2 == 3:
            co2 ='Naranja'
            horale2='#f2863e'
        elif color2 == 4:
            co2 ='Amarillo'
            horale2='#f2e23e'
        elif color2 == 5:
            co2 ='Verde'
            horale2='#bbe231'
        elif color2 == 6:
            co2 ='Azul'
            horale2='#71a4e2'
        elif color2 == 7:
            co2 ='Violeta'
            horale2='#a571e2'
        elif color2 == 8:
            co2 ='Gris'
            horale2='#dbd5e2'
        else:
            co2 ='Blanco'
            horale2='#fefbfb'
        
        if color3 == 1:
            co3='Negro'
            horale3='#565f5b'
        elif color3 == 10:
            co3 ='Cafe'
            horale3='#a05b3d'
        elif color3 == 100:
            co3 ='Rojo'
            horale3='#ea1e1b'
        elif color3 == 1000:
            co3 ='Naranja'
            horale3='#f2863e'
        elif color3 == 10000:
            co3 ='Amarillo'
            horale3='#f2e23e'
        elif color3 == 100000:
            co3 ='Verde'
            horale3='#bbe231'
        elif color3 == 1000000:
            co3 ='Azul'
            horale3='#71a4e2'
        elif color3 == 1000000:
            co3 ='Violeta'
            horale3='#a571e2'
        elif color3 == 100000000:
            co3 ='Gris'
            horale3='#dbd5e2'
        else: 
            co3 ='Blanco'
            horale3='#fefbfb'
            
        if tolerancia == 5:
            tol = 'Oro'
            maxim = total+(total*.05)
            minm = total-(total*.05)
            tole='#cfc436'
        elif tolerancia == 10:
            tol= 'Plata'
            maxim = total+(total*.10)
            minm = total-(total*.10)
            tole='#e4e4e4'
        else :
            tol='Quien sabe como le hicite'
            
        print('max {}'.format(maxim))    
        print('min {}'.format(minm)) 
    
        
        
    print('dkd {}'.format(total))        
    return render_template("resistencia.html",form=resistencia_clase,color1=color1, color2=color2, color3=color3, tolerancia=tolerancia, total=total,maxim=maxim, minm=minm, co1=co1,co2=co2,co3=co3,tol=tol,horale=horale, horale2=horale2,horale3=horale3,tole=tole)
        
        
        
    
        
if __name__=="__main__":
    app.run(debug=True)
        