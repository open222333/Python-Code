from flask_mongoengine import MongoEngine
from datetime import datetime
from flask import Flask

app = Flask(__name__)
db = MongoEngine()
db.init_app(app)


class TempUploadTencent(db.Document):
    code = db.StringField(required=True, unique=True)
    is_upload = db.BooleanField(default=False)
    data = db.DictField()
    locked = db.BooleanField(default=False)
    status = db.StringField(default='ready')  # ready running completed
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.now)
    meta = {
        'indexes': [
            'is_upload',
            'creation_date',
            'modified_date'
        ]
    }

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(TempUploadTencent, self).save(*args, **kwargs)


test = TempUploadTencent.objects(code="TEST-11121").first()
if test is None:
    test = TempUploadTencent(code="TEST-11121", is_upload=True, data={})
test.save()
