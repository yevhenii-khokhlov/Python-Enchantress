FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python python-pip
RUN pip install flask
COPY simple_flask_app.py /opt/
ENTRYPOINT FLASK_APP=/opt/simple_flask_app.py flask run --host=0.0.0.0 --port=8080
