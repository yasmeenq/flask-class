from utils.dal import DAL 
from utils.image_handler import ImageHandler
class ProductLogic:
    def __init__(self):
        self.dal = DAL() 

    def get_all_products(self):
        sql = "select * from products1"
        return self.dal.get_table(sql)
    
    def get_one_products(self, id):
        sql = "select * from products1 where id = %s"
        return self.dal.get_scalar(sql, (id,))
    
    def add_product(self, product):
        image_name = ImageHandler.save_image(product.image)
        sql = "INSERT INTO products1(name, price, stock, image_name) values(%s, %s, %s, %s)"
        return self.dal.insert(sql,(product.name, product.price, product.stock, image_name))

    
    def close(self):
        self.dal.close()
