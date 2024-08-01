from flask import Blueprint, render_template, send_file, url_for, redirect, request, session 
from facades.products_facade import ProductsFacade
from utils.image_handler import ImageHandler
from models.client_error import * 
from facades.auth_facade import * 
from models.role_model import * 

products_blueprint = Blueprint("products_view", __name__)
facade = ProductsFacade() 
auth_facade = AuthFacade()

@products_blueprint.route("/products")
def list():
    all_products = facade.get_all_products() 
    # print(all_products)
    return render_template("products.html", products = all_products,active="products")


@products_blueprint.route("/products/details/<int:id>")
def details(id):
    try:
        one_product = facade.get_one_product(id)
        return render_template("details.html", product = one_product, current_user = session.get('current_user'), admin=RoleModel.Admin.value )
    except ResourceNotFoundError as err:
        return render_template("404.html", error=err.message)



 
@products_blueprint.route("/products/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)
  

@products_blueprint.route("/products/new", methods=["GET", "POST"])

def insert():
    try:
        auth_facade.block_anonymous()
        if(request.method=="GET"): return render_template("insert.html",active="new")
        facade.add_product()
        return redirect(url_for("products_view.list"))
    except AuthError as err:
        return redirect("auth_view.login",error=err.message, credentials={})
    except ValidationError as err:
        return render_template("insert.html",error=err.message)

@products_blueprint.route("/products/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    try:
        auth_facade.block_non_admin()
        if(request.method=="GET"): 
            one_product = facade.get_one_product(id)
            return render_template("edit.html", product=one_product)
        facade.update_product()
        return redirect(url_for("products_view.list"))
    except AuthError as err:
        all_products = facade.get_all_products() 
        return render_template("products.html", error=err.message, products = all_products)
    except ValidationError as err:
        return render_template("edit.html",error=err.message)


@products_blueprint.route("/products/delete/<int:id>")
def delete(id):
    try: 
        auth_facade.block_non_admin()
        facade.delete_product(id)
        return redirect(url_for("products_view.list"))
    except AuthError as err:
        all_products = facade.get_all_products() 
        return render_template("products.html", error=err.message, products = all_products)


# @products_blueprint.route("/products/save", methods=["POST"])
# def save():
#     facade = ProductsFacade() 
#     facade.add_product()
#     return redirect(url_for("products_view.list"))
