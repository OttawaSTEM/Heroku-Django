# This django skeleton is suitable to Heroku and Azure Web App 
## 1. Heroku
1.1 Create App from Heroku

1.2 Connect Github in Heroku

1.3 prepare Porcfile and requirements.txt
web: daphne mysite.asgi:application --port $PORT --bind 0.0.0.0 -v2

1.4 Django Database
need include basic db.sqlite3 in git
default user account: admin/admin


## 2 Azure Web App
Azure Web App launch Django
```
$ python manager.py runserver
```

# Deploy options
DJANGO_ENVIRONMENT = Development:
    mysite.settings.development
DJANGO_ENVIRONMENT = Container:
    mysite.settings.container
DJANGO_ENVIRONMENT = VirtualMachine:
    mysite.settings.virtualmachine