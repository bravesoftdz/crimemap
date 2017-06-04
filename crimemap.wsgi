import sys
import os
import site


sys.path.insert(0, "/var/www/crimemap")

activate_env = os.path.expanduser(os.path.join(os.path.dirname(__file__), '/var/www/env/bin/activate_this.py'))
execfile(activate_env, dict(__file__=activate_env))


from crimemap import app as application

