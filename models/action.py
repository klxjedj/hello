from ..models import db

class Action(db.DynamicDocument):
    userTel=db.IntField()
    timeStamp=db.IntField()
    actionType=db.StringField()
    targetindex=db.IntField()
    currentAttr=db.IntField()