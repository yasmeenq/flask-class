from flask import Flask
from views.home_view import home_blueprint
from views.about_view import about_blueprint

app = Flask(__name__)

app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)