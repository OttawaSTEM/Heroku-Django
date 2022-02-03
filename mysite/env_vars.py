# Use 12factor inspired environment variables or from a file
import os
from pathlib import Path

import environ
env = environ.Env()

# BASE_DIR = Path(__file__).resolve(strict=True).parent
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

if os.environ.get('DJANGO_ENVIRONMENT') == 'Deployment':
    environ.Env.read_env()
    # env_file = BASE_DIR.joinpath('django_skeleton', 'settings', 'local.env')
    # if os.path.exists(env_file):
    #     environ.Env.read_env(str(env_file))
    DEBUG = False           # Must run python manage.py collect static, otherwise cause Server Error (500)
    CSRF_TRUSTED_ORIGINS = ['https://ottawastem-django.herokuapp.com']      # When DEBUG=False in Deployment
else:
    # Ideally move env file should be outside the git repo, i.e. BASE_DIR.parent.parent
    # env_file = BASE_DIR.joinpath('django_skeleton', 'settings', 'local.env')
    env_file = BASE_DIR.joinpath('mysite', 'local.env')
    if os.path.exists(env_file):
        environ.Env.read_env(str(env_file))
    DEBUG = True
