from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,TelField,IntegerField,FloatField
from wtforms import EmailField
from wtforms.validators import DataRequired, Email


class UserForm(Form):
    distancia1= IntegerField('distancia1')
    distancia2= IntegerField('distancia2')
    distancia3= IntegerField('distancia3')
    distancia4= IntegerField('distancia4')
    
class Resis(Form):
    color1= IntegerField('color1')
    color2= IntegerField('color2')
    color3= IntegerField('color3')
    tolerancia= IntegerField('tolerancia')
    maxim= StringField('maxim')
    minm= StringField('minm')
    