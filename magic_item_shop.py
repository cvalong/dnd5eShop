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
        
location_list = ["Thorp", "Hamlet", "Village", "Small Town", "Large Town", 
                "Small City", "Large_City", "Metropolis"]

shop_type_list =["Trader", "Armorer", "Weaponsmith",
                "Alchemist", "Scribe", "Wandwright"]

def random_selector(list, start_index= 0):
        return list[randint(start_index, len(list)-1)]

def random_location():
        return random_selector(location_list)

def random_shop_type():
        return random_selector(shop_type_list)

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

items_header, items_rows = csv_reader('test_items_dungeons_5e.csv')
print(random_selector(items_rows))