from ..models import db

class Info(db.DynamicDocument):
    userTel=db.IntField()
    userUUID=db.StringField()
    screenWidth=db.IntField()
    screenHeight=db.IntField()
    pixelRatio=db.FloatField()
    group=db.IntField()
    ip=db.StringField()