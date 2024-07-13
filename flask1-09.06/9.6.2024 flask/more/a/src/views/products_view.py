from flask import Blueprint, render_template

# Managing the entire view
products_blueprint = Blueprint("products_view", __name__) # "products_view" is the name of the view


@products_blueprint.route("/products") # Route
def list(): # View Function
    return render_template("products.html")

