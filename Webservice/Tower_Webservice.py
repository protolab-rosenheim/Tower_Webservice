import flask
import flask_restless
from flask_cors import CORS

from Webservice.DatabaseSetup import DatabaseSetup
from Webservice.DbModels import *
from Webservice.__init__ import *


app = flask.Flask(__name__)
app.config['DEBUG'] = debug_mode

app.config['SQLALCHEMY_DATABASE_URI'] = db_connect_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)

# Create the database tables.
db.create_all()

DatabaseSetup(db, modules_conf).setup_modules()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

api_version_string = '/api/v1'

# Create API endpoints, which will be available at /api/v1/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Module, methods=['GET', 'POST', 'PUT', 'DELETE'], url_prefix=api_version_string)
manager.create_api(Slot, methods=['GET', 'POST', 'PUT', 'DELETE'], url_prefix=api_version_string)
manager.create_api(Coating, methods=['GET', 'POST', 'PUT', 'DELETE'], url_prefix=api_version_string)

cors = CORS(app)

app.run('0.0.0.0', port=5000)
