1. Create App from Heroku

2. Connect Github in Heroku

3. prepare Porcfile and requirements.txt
web: daphne mysite.asgi:application --port $PORT --bind 0.0.0.0 -v2

# Django Database
need include basic db.sqlite3 in git
default user account: admin/admin
