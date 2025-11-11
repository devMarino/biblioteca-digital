from flask import Flask #import Flask from flask package
from flask_sqlalchemy import SQLAlchemy #import SQLAlchemy from flask_sqlalchemy package
from flask_migrate import Migrate #import migrate from flask_migrate package
from config import Config #import configs from config.py file

migrate = Migrate() #create an instance of Migrate
db = SQLAlchemy() #create an instance of SQLAlchemy

#define a function to create the Flask application
def create_app(Config=Config):
#create an instance of Flask application
    app = Flask(__name__)
    
#load configurations from Config class
    app.config.from_object(Config)
#initialize the database with the Flask application
    db.init_app(app)
    #import all blueprints
    from .routes import ALL_BLUEPRINTS

    #import list of blueprints and their url prefixes
    for blueprint, url_prefix in ALL_BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix=url_prefix)

#initialize migrate with the Flask application and database
    migrate.init_app(app, db)
    return app

if __name__ == '_main__':
    app = create_app()
    app.run(debug=True) #run the aplpication in debug mode 