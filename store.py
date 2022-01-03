import product
class Store:
    def __init__(self, name):
        self.name=name
        self.product_list=[]
    def add_product(self, name, price, category):
        new_product = product.Product(name,price,category)
        self.product_list.append(new_product)
    def sell_product(self,id):
        sold_item=self.product_list.pop(id)
        print('The item', sold_item.name, sold_item.price, sold_item.category, 'has been sold')
    def inflation(self, percent_increase):
        for product in self.product_list:
            product.update_price(percent_increase, True)
    def set_clearance(self, category, percent_discount):
        for product in self.product_list:
            if product.category == category:
                product.update_price(percent_discount, False)
    def show_product_list(self):
        for j in self.product_list:
            print(j.name, j.price, j.category)


