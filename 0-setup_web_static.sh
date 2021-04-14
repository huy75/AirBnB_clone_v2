#!/usr/bin/env bash
# Sets up web servers for deployment

# install nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# Create folders
sudo mkdir --parents /data/web_static/shared/
sudo mkdir --parents /data/web_static/releases/test/

# Create fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the data folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

# Routing to web static
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart

# Always exit successfully
exit 0
