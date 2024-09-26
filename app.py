from flask import Flask
from controllers.target_controller import target_blueprint
from repository.db import create_tables
from model import *

app = Flask(__name__)

if __name__ == '__main__':
    create_tables()
    app.register_blueprint(target_blueprint, url_prefix="/api/targets")
    app.run(debug=True)
