from flask import Flask, render_template
from views.home_view import home_blueprint
from views.about_view import about_blueprint
from views.products_view import products_blueprint
from views.auth_view import auth_blueprint
from logging import getLogger, ERROR
from utils.app_config import AppConfig

app = Flask(__name__)
app.secret_key = AppConfig.session_secret_key
app.register_blueprint(home_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(auth_blueprint)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


@app.errorhandler(Exception)
def catch_all(error):
    print(error)
    return render_template('500.html', error=error)

# werkzeug - ארגז כלים 
getLogger("werkzeug").setLevel(ERROR)


# admin - delete 
# user make successfully  login - update , insert
# not login - view only 