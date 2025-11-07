from Flask import Flask #import Flask from flask package
from flask_sqlalchemy import SQLAlchemy #import SQLAlchemy from flask_sqlalchemy package
from flask_migrate import Migrate #import migrate from flask_migrate package
from config import Config #import configs from config.py file

migrate = Migrate() #import Migrate from flask_migrate package
db = SQLAlchemy() #create an instance of SQLAlchemy

#define a function to create the Flask application
def create_app(Config=Config):
#create an instance of Flask application
    app = Flask(__name__) 
#load configurations from Config class
    app.config.from_object(Config)
#initialize the database with the Flask application
    db.init_app(app)
#initialize migrate with the Flask application and database
    migrate.init_app(app, db)
    return app

migrate = Migrate(app, db) #create an instance of Migrate to handle database migrations
if __name__ == '_main__':
    app.run(debug=True) #run the aplpication in debug mode 