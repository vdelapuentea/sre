FROM python:latest

EXPOSE 80
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

CMD ["python", "app.py"]
