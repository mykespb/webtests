virtualenv --python=python2 tryonce --no-site-packages
chown myke:www-data -R .htaccess
pip freeze > requirements.txt
pip install bottle
source bin/activate
deactivate
