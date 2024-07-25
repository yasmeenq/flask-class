from flask import Blueprint, render_template, send_file, url_for, redirect, request
from facades.auth_facade import AuthFacade
from models.client_error import * 
auth_blueprint=Blueprint("auth_view", __name__)

facade = AuthFacade() 

@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "GET": return render_template("register.html",active="register")
        facade.register() 
        return redirect(url_for("home_view.home"))
    except ValidationError as err:
        return render_template("register.html", error = err.message)

