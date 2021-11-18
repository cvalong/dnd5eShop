from random import randint

class magic_item_shop:
    def __init__(self, name, location, shop_type, 
                location_description="", shop_description="", shopkeeper="",item_stock=[]):
        self.name = name
        self.location = location
        self.shop_type = shop_type
        self.location_description = location_description
        self.shop_description = shop_description
        self.shopkeeper = shopkeeper
        self.item_stock = item_stock

location_dict = {1: "Thorp", 2: "Hamlet", 3: "Village", 4: "Small Town", 5: "Large Town", 
                6: "Small City", 7: "Large_City", 8: "Metropolis"}

shop_type_dict = {1: "Trader", 2: "Armorer", 3: "Weaponsmith",
                4: "Alchemist", 5: "Scribe", 6: "Wandwright"}

def stock_reader():
        pass

def random_location():
        return location_dict[randint(1,len(location_dict))]

def random_shop_type():
        return shop_type_dict[randint(1, len(shop_type_dict))]

# magic_shop = magic_item_shop("Benny's Booming Bargains", "Metropolis", "Armorer")
# print(random_location())

