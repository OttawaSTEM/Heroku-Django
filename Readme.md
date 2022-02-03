# Deploy in Heroku from Github

# Create App from Heroku

# Connect Github in Heroku

# Porcfile
web: gunicorn --pythonpath="$PWD/mysite" mysite.wsgi
web: daphne mysite.asgi:application

# Django Database
need include basic db.sqlite3 in git
