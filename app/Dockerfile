FROM python:3.9.5-slim-buster
WORKDIR /usr/src/app
#RUN apt-get update
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "./bin/wait-for-it.sh", "openldap:389", "-s", "-t", "120", "--", "./bin/start.sh" ]