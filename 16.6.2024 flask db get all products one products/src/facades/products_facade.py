from logic.products_logic import ProductLogic 

class ProductsFacade:

    def __init__(self):
        self.logic = ProductLogic() 

    def get_all_products(self):
        return self.logic.get_all_products() 
    
    def get_one_product(self, id):
        return self.logic.get_one_products(id)
    
    def close(self):
        self.logic.close() 