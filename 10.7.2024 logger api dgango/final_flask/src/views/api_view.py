from flask import Blueprint,jsonify, render_template, send_file, url_for, redirect, request, session , make_response
from facades.products_facade import ProductsFacade
from utils.image_handler import ImageHandler
from models.client_error import * 
from facades.auth_facade import * 
from models.role_model import * 
from utils.logger import Logger
from models.status_code import StatusCode

api_blueprint = Blueprint("api_view", __name__) 

product_facade = ProductsFacade() 

@api_blueprint.route("/api/products")
def products():
    products = product_facade.get_all_products() 
    return jsonify(products)


@api_blueprint.route("/api/product/<int:id>")
def product(id):
    try:
        product = product_facade.get_one_product(id)
        return jsonify(product)
    except ResourceNotFoundError as err:
        Logger.log(err.message)
        json = jsonify({"error":err.message})
        return make_response(json, StatusCode.NotFound) 
        


