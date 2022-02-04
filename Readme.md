# Heroku
1. Create App from Heroku

2. Connect Github in Heroku

3. prepare Porcfile and requirements.txt
web: daphne mysite.asgi:application --port $PORT --bind 0.0.0.0 -v2

4. Django Database
need include basic db.sqlite3 in git
default user account: admin/admin


# This also suitalbe to Azure Web App deployment


# Deploy options:
DJANGO_ENVIRONMENT = Development:
    mysite.settings.development
DJANGO_ENVIRONMENT = Container:
    mysite.settings.container
DJANGO_ENVIRONMENT = VirtualMachine:
    mysite.settings.virtualmachine