from flask import Flask,render_template, request

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
        
if __name__=="__main__":
    app.run(debug=True)
        