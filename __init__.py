from flask import Flask
from flask_wtf import CSRFProtect
from flask_sqlalchemy  import SQLAlchemy
import config




rand = Flask(__name__,instance_relative_config=True)
csrf = CSRFProtect(rand)
rand.config.from_pyfile("config.py")
rand.config.from_object(config.ProductionConfig)
db = SQLAlchemy(rand)


from personal import myroute










