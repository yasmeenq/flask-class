from utils.dal import DAL 

class ProductLogic:
    def __init__(self):
        self.dal = DAL() 

    def get_all_products(self):
        sql = "select * from products1"
        return self.dal.get_table(sql)
    
    def get_one_products(self, id):
        sql = "select * from products1 where id = %s"
        return self.dal.get_scalar(sql, (id,))
    
    def close(self):
        self.dal.close()
