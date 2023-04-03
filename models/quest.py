from ..models import db

class Quest(db.DynamicDocument):
    userTel=db.IntField()
