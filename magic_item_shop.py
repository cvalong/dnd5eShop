class magic_item_shop:
    def __init__(self, name, location, shop_type, 
                location_description="", shopkeeper="",item_stock=[]):
        self.name = name
        self.location = location
        self.shop_type = shop_type
        self.location_description = location_description
        self.shopkeeper = shopkeeper
        self.item_stock = item_stock

magic_shop = magic_item_shop("Benny's Booming Bargains", "Metropolis", "Armorer")
print(magic_shop.name)
print(magic_shop.location)
print(magic_shop.shop_type)