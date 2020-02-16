from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import config
app.config.from_object(config.Config)


from app import routes, models