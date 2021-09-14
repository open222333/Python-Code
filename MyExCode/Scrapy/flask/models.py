from datetime import datetime
from flask import mongo as db


class Models(db.Document):
    post_id = db.IntField(required=True)
    title = db.StringField()
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.now)
    meta = {
        'indexes': [
            'post_id',
            'title',
            'creation_date',
            'modified_date',
        ]
    }

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(Models, self).save(*args, **kwargs)
