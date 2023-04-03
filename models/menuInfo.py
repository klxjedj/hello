from ..models import db

class MenuInfo(db.DynamicDocument):
    userTel=db.IntField()
