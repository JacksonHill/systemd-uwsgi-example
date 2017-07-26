# systemd-uwsgi-example
Example config files for running Flask application using 
uWSGI application server in emperor mode, with nginx as a frontend.

## Installation:

**Install apropriate packages:**
* python
* python-pip
* python-virtualenv
* nginx
* gcc (for uwsgi compilation)

**Copy nginx config**
Copy example_nginx.conf to /etc/nginx/conf.d

**Copy systemd config**
Copy uwsgi-example to /usr/bin
Copy uwsgi-example.service to /usr/lib/systemd/system

**Create directories for application:**
```
mkdir -p /opt/example/log
mkdir -p /opt/example/venv
mkdir -p /opt/example/run
```

**Copy application files:**
* app.py and requirements.txt to /opt/example
* example.ini to /opt/example/run

**Install and configure application virtualenv:**
```
virtualenv /opt/example/venv
/opt/example/venv/bin/pip install -r /opt/example/requirements.txt
```

**Fix permissions:**
```
chown -R nginx:nginx /opt/example
```

**Enable service:**
```
systemctl enable uwsgi-example.service
```

**Run the service:**
```
service uwsgi-example start
```

**Navigate to** http://127.0.0.1:8080

## Horizontally scaling single application
If your application can be run simultaneously, by just invoking it multiple times from the same directory, you simply have to:
* add another copy of .ini file with different port
* add another entry in nginx upstream config with the new port number
* copy new .ini file to vassals dir (emperor will spawn new instance of your app.)
* reload nginx to pick-up new config
