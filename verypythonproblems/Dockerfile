FROM python:3.6
LABEL maintainer="verypythonproblems"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

COPY . /code/
WORKDIR /code/

RUN python manage.py makemigrations
RUN python manage.py migrate

RUN useradd coderedcms
RUN chown -R coderedcms /code
USER coderedcms

EXPOSE 8000
CMD exec gunicorn verypythonproblems.wsgi:application --bind 0.0.0.0:8000 --workers 3
