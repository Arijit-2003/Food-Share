release: python manage.py migrate --noinput && python manage.py ensure_admin
web: gunicorn Food_Management.wsgi
