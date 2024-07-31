# rick-and-morthy

### How to run
On Windows
- Create venv: python -m venv venv
- Activate it: .venv\Scripts\activate
- Install requirements: pip install -r requirements.txt
- Run migrations: python manage.py migrate
- Run Redis Server: docker run -d -p 6379:6379 redis
- Run celery for task handling: celery -A rick_and_morthy_api worker -l INFO
- Run celery beat for task scheduling: celery -A rick_and_morthy_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
- Create schedule for running in database
- Run app: python manage.py runserver
