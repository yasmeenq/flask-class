from logic.products_logic import ProductLogic 
from flask import request
from models.product_model import ProductModel

class ProductsFacade:

    def __init__(self):
        self.logic = ProductLogic() 

    def get_all_products(self):
        return self.logic.get_all_products() 
    
    def get_one_product(self, id):
        return self.logic.get_one_products(id)
    

    def add_product(self):
        name = request.form.get("name") # <input type=text....name = "name" > 
        price = request.form.get("price") # <input type=number....name = "price" > 
        stock = request.form.get("stock") # <input type=text....name = "stock" > 
        image = request.files["image"]  # <input type="file" name="image" >  
        product = ProductModel(None, name, price, stock, image)
        self.logic.add_product(product)


    def update_product(self):
        id = request.form.get("id") # <input type=hidden....name = "id" > 
        name = request.form.get("name") # <input type=text....name = "name" > 
        price = request.form.get("price") # <input type=number....name = "price" > 
        stock = request.form.get("stock") # <input type=text....name = "stock" > 
        image = request.files["image"]  # <input type="file" name="image" >  
        product = ProductModel(id, name, price, stock, image)
        self.logic.update_product(product)


    def delete_product(self, id):
        self.logic.delete_product(id)

        
    def close(self):
        self.logic.close() 