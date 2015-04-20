Configuration Services setup requirement:

install Python 2.7.6 - https://www.python.org/download/releases/2.7.6/
install django 1.7.1 - https://www.djangoproject.com/download/
pip install Django==1.7   -- 1.8 was giving PK error on .MetaDict

check django version from python console:
import django
django.VERSION


install pydev eclipse python integration
install MongoEngine -
    pip install mongoengine

install mongod and run it locally   # install 2.6.9 version. 3.0 is giving error on PK

install django rest framework:
http://www.django-rest-framework.org/#installation
add Restframework to set:

pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

Create Database on Mongodb:
mongo
use cfg

create, update, delete, lock config
when config is locked, it cannot be edited, but still removed?
appid, version, build, platform is unique index
add rest api to return data based on the unique index
add authentication

Runserver: python manage.py runserver

create a user in mongodb:

python manage.py shell
>>> from django.contrib.auth import get_user_model
>>> user = get_user_model().objects.create_user('admin','nahrinrs@yahoo.com','password')
>>>from django.contrib import auth
>>>user = auth.authenticate(username="admin", password="password")
>>>print user
>>>print user.is_active


pip install -U django-cacheops
http://127.0.0.1:8000/login

