Configuration Services setup requirement:

install Python 2.7.6 - https://www.python.org/download/releases/2.7.6/
install django 1.7.1 - https://www.djangoproject.com/download/

check django version from python console:
import django
django.VERSION


install pydev eclipse python integration
install MongoEngine -
sudo pip install mongoengine
install mongod and run it locally 
create, update, delete, lock config
when config is locked, it cannot be edited, but still removed?
appid, version, build, platform is unique index
add rest api to return data based on the unique index
install django rest framework:
http://www.django-rest-framework.org/#installation

add authentication
add Restframework to set:

pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

Runserver: python mange.py runserver
create a user in mongodb: 
python manage.py shell
>>> from django.contrib.auth import get_user_model
>>> get_user_model().objects.create_user('admin','nahrin@gaiaonline.com','password')


pip install -U django-cacheops

