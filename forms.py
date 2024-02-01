from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField,TelField,IntegerField
from wtforms import EmailField
from wtforms.validators import DataRequired, Email


class UserForm(Form):
    distancia1= IntegerField('distancia1')
    distancia2= IntegerField('distancia2')
    distancia3= IntegerField('distancia3')
    distancia4= IntegerField('distancia4')
    