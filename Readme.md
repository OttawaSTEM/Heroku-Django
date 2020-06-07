# Deploy in Heroku from Github
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/OttawaSTEM/Heroku-Django.git/)

# Create App from Heroku

# Connect Github in Heroku fo

# runtime.txt
python-3.7.7

# Porcfile
web: gunicorn --pythonpath="$PWD/mysite" mysite.wsgi

# Django Collect Static
Add to the top of settings.py 
import django_heroku

Add to the bottom of setting.py 
django_heroku.settings(locals())
