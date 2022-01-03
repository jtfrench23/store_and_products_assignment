import product
import store
great_buy=store.Store('Great Buy')
great_buy.add_product('Macbook Air M1', 1000, 'computer')
great_buy.add_product('JT Custom PC', 1100, 'computer')
great_buy.add_product('Vizio 4k TV', 400, 'TV')
great_buy.add_product('Samsung Smart 4k TV', 600, 'TV')
great_buy.show_product_list()
great_buy.sell_product(1)
great_buy.inflation(.25)
great_buy.show_product_list()
great_buy.set_clearance('TV',.5)
great_buy.show_product_list()