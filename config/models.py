from mongoengine import *
from configServices.settings import DBNAME

connect(DBNAME)

class Config(Document):
    appId = StringField(max_length = 500, required=True) # ravel, Unravel, ....
    version = StringField(max_length = 200, required=True)  # app version, like 1.1
    build = StringField(max_length = 100, required=True)  # app build, like 1, 2, 3, ...
    platform = StringField(max_length=500, required=True)  # platform like, Andriod, iPhone,... can be validated against useragent
    last_update = DateTimeField(required=True) 
    islocked =  BooleanField(default=False, required=True)
    content = StringField(max_length = 5000) # key/value config info
    
    meta = {
        'indexes': [
            {'fields': ('appId', 'version', 'build', 'platform'), 'unique': True}
        ]
    }
   
