import os
import sys

def main():
    if os.environ.get('DJANGO_ENVIRONMENT') == 'Development':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
        # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.development')
    elif os.environ.get('DJANGO_ENVIRONMENT') == 'Deployment':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.deployment')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.production')


    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
