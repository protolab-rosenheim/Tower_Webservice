from pathlib import Path
import os
import ast

import yaml
from sqlalchemy.engine import url

# ENV only used if we run the code outside docker
try:
    config_folder = os.environ['VOLUME_DIR'] + '/tower_webservice'
except KeyError:
    config_folder = '/usr/src/app/conf'

modules_conf_path = Path(config_folder + '/modules.yml')
with open(modules_conf_path) as f:
    modules_conf = yaml.safe_load(f)

# DB setup
db_connect_url = url.URL(drivername=os.environ['DATABASE_DIALECT'],
                         username=os.environ['DATABASE_USER'],
                         password=os.environ['DATABASE_PASSWORD'],
                         host=os.environ['DATABASE_HOSTNAME'],
                         port=os.environ['DATABASE_PORT'],
                         database=os.environ['DATABASE_NAME'])

debug_mode = ast.literal_eval(os.environ['DEBUG_MODE'])
