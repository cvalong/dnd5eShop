from random import randint

class magic_item_shop:
    def __init__(self, name, location_description="", 
                shop_description="", shopkeeper="",item_stock=[]):
        self.name = name
        self.location = random_location()
        self.shop_type = random_shop_type()

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

def random_selector(dict):
        return dict[randint(1,len(dict))]

def random_location():
        return random_selector(location_dict)

def random_shop_type():
        return random_selector(shop_type_dict)