# Stage 1: Build Stage
FROM python:slim-bullseye

WORKDIR /python-docker

COPY req.txt requirements.txt
#RUN apt-get update -y
#RUN apt-get update && apt-get install -y python3-pip
#RUN apt-get autoremove -y
#RUN apt-get clean
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 5000

CMD [ "python3", "app.py"]