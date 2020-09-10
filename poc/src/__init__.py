from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config
from flask_migrate import Migrate

poc = Flask(__name__)

poc.config.from_object(config.StagingConfig)
poc.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(poc)
migrate = Migrate(poc, db)

@poc.errorhandler(404)
def not_found(error):
    return '404', 404

from src.app import flaskpoc

poc.register_blueprint(flaskpoc)
db.create_all()
