from ..models import db

class Menu(db.DynamicDocument):
    group=db.IntField()
