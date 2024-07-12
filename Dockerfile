FROM python:latest

COPY * /var/www/app/

RUN pip install flet \
    && pip install requests 

EXPOSE 