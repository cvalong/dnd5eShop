import csv
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

def random_selector(dict, start_index= 1):
        return dict[randint(start_index, len(dict))]

def random_location():
        return random_selector(location_dict)

def random_shop_type():
        return random_selector(shop_type_dict)

def random_item():
        pass

def csv_reader(sheet):
        file = open(sheet)
        csvreader = csv.reader(file)
        header =[]
        header = next(csvreader)
        rows =[]
        for row in csvreader:
                rows.append(row)
        file.close()
        return header, rows

def stock_list_generator():
        pass

csv_contents = csv_reader('test_items_dungeons_5e.csv')
print(csv_contents)