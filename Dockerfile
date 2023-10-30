FROM python:alpine

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
RUN pip3 install gunicorn
COPY . /app

WORKDIR /app

CMD ["python3", "-m", "gunicorn", "-w", "1", "--bind=0.0.0.0:5050", "wsgi:app"]
