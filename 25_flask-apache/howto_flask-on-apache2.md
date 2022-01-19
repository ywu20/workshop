# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time.

### Estimated Time Cost: 30 minutes

### Prerequisites:
- Install and set up Apache2.
- Updated all your packages.

1. Install mod_wsgi and pip:
```
sudo apt-get install libapache2-mod-wsgi-py3 python-dev
sudo apt-get install python-pip
```
2. Enable mod_wsgi: `sudo a2enmod wsgi`
3. Create this file structure in the /var/www directory:
```
|----<FlaskAppName>
|---------<FlaskAppName>
|--------------__init__.py
|--------------static
|--------------templates
```
Make sure you named the file you want to run `__init__.py`.
4. Create a virtual environment in /var/www/<FlaskAppName>/<FlaskAppName>.
5. Enable the virtual environment, and install Flask with `pip install flask`.
	- If this doesn't work, skip this step and install Flask globally or use `sudo su` to operate everything in superuser mode.
6. Place some example code in `__init__.py`:
```python
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
if __name__ == "__main__":
    app.run()
```
7. Create a site configuration file:
`sudo nano /etc/apache2/sites-available/<FlaskAppName>.conf`
8. Add this to the config file:
```
<VirtualHost *:80>
		ServerName <DropletIPAddress>
		ServerAdmin <Email>
		WSGIScriptAlias / /var/www/<FlaskAppName>/<flaskappname>.wsgi
		<Directory /var/www/<FlaskAppName>/<FlaskAppName>/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/<FlaskAppName>/<FlaskAppName>/static
		<Directory /var/www/<FlaskAppName>/<FlaskAppName>/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
9. Enable the virtual host: `sudo a2ensite <FlaskAppName>`. You need to do this everytime you switch to another flask app you want to serve.
10. Create a wsgi file called <flaskappname>.wsgi in /var/www/<FlaskAppName>. Now your file structure should look like this:
```
|----<FlaskAppName>
|---------<FlaskAppName>
|--------------__init__.py
|--------------static
|--------------templates
|---------<flaskappname>.wsgi
```
11. Add this to the wsgi file:
```python
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/<FlaskAppName>/")

from FlaskApp import app as application
application.secret_key = <secretkey>
```
12. Restart Apache so the changes take effect: `sudo service apache2 restart `. You need to restart everytime you changed something!
13. Hopefully it works!

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps

---

Accurate as of (last update): 2022-01-19

#### Contributors:  
Michael Borczuk, pd2  
Yuqing Wu, pd2  
