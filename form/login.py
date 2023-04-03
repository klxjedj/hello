from flask_wtf import FlaskForm
from wtforms import TelField,SubmitField

class LoginForm(FlaskForm):
    tel=TelField("",id='tel')
    sub=SubmitField('进入实验')