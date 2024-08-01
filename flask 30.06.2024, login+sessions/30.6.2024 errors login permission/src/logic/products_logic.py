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



    def update_product(self, product):
        old_image_name = self.get_old_image_name(product.id)
        image_name = ImageHandler.update_image(old_image_name, product.image) # 
        sql = "UPDATE products1 set name=%s, price = %s , stock=%s, image_name=%s where id=%s"
        self.dal.update(sql, (product.name, product.price, product.stock, image_name, product.id))
    

    def get_old_image_name(self, id):
        sql = "SELECT image_name from products1 where id=%s"
        result = self.dal.get_scalar(sql, (id,)) 
        return result["image_name"]


    def delete_product(self, id):
        image_name = self.get_old_image_name(id)
        ImageHandler.delete_image(image_name)
        sql = "DELETE FROM products1 where id=%s"
        self.dal.delete(sql, (id, ))

    def close(self):
        self.dal.close()
