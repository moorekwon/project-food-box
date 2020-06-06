daemon = False
chdir = '/srv/foodbox/app'
bind = 'unix:/run/foodbox.sock'
accesslog = '/var/log/gunicorn/foodbox-access.log'
errorlog = '/var/log/gunicorn/foodbox-error.log'
