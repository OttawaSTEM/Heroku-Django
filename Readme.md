# Deploy in Heroku from Github

# Create App from Heroku

# Connect Github in Heroku

# Porcfile
web: gunicorn --pythonpath="$PWD/mysite" mysite.wsgi

# Django Collect Static
Add to the top of settings.py 
import django_heroku

Add to the bottom of setting.py 
django_heroku.settings(locals())


python manage.py migrate
python manage.py createsuperuser
