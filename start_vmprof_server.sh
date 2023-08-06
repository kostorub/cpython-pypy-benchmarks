cd ~/git/vmprof-server
source ~/git/vmprof-server/.venv/bin/activate
python manage.py runserver -v 3

# python -m vmprof --web --web-url http://127.0.0.1:8000 src/app.py