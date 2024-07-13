from flask import Flask
from views.home_view import home_blueprint
app = Flask(__name__)

app.register_blueprint(home_blueprint)