# systemd-uwsgi-example
Example config files for running Flask application using 
uWSGI application server in emperor mode, with nginx as a frontend.

Installation:

Install apropriate packages:
* python
* python-pip
* python-virtualenv
* nginx
* gcc (for uwsgi compilation)

Copy example_nginx.conf to /etc/nginx/conf.d
Copy uwsgi-example to /usr/bin
Copy uwsgi-example.service to /usr/lib/systemd/system

Create directories for application:
* mkdir -p /opt/example/log
* mkdir -p /opt/example/venv
* mkdir -p /opt/example/run

Copy files:
* app.py and requirements.txt to /opt/example
* example.ini to /opt/example/run


Install and configure virtualenv:
virtualenv /opt/example/venv
/opt/example/venv/bin/pip install -r /opt/example/requirements.txt

Fix permissions:
chown -R nginx:nginx /opt/example

Enable service: 
systemctl enable uwsgi-example.service

Run the service:
service uwsgi-example start

Navigate to localhost:8080
