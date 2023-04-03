from flask_wtf import FlaskForm
from wtforms import StringField

class InfoForm(FlaskForm()):
    id=StringField(())
    info=StringField()