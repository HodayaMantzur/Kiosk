from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from config import Config
    
# configuring flask
app = Flask(__name__)

# לוקח את כל המידע מהמודולס 
app.config.from_object(Config)
db = SQLAlchemy(app)

from routes import *

# Initialize the database תיצור טבלאות
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)