FROM python:3.12

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

RUN python api_testing/manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python api_testing/manage.py shell

EXPOSE 8000

CMD ["python", "api_testing/manage.py", "runserver", "0.0.0.0:8000"]