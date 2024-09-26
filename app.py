from flask import Flask
from controllers.target_controller import target_blueprint
from repository.db import create_tables, drop_tables
from model import *

app = Flask(__name__)

if __name__ == '__main__':
    create_tables()
    app.register_blueprint(target_blueprint, url_prefix="/api/mission")
    app.run(debug=True)

    # drop_tables()
