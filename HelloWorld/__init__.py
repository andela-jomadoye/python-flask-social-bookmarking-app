import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = b'U[\ty\x0e\xbe\x83a\xe3\xa9\x19\x13\xf2\xfcOB;\x10~\xbd~\xfc`\xac'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')

# toolbar = DebugToolbarExtension(app)
db = SQLAlchemy(app)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.init_app(app)

import HelloWorld.views
import HelloWorld.models
