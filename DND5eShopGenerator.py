'''
--GUI??--
        run function for magic_shop_generator and store in new magic_item_shop
        
    Location Dropbox
    Type Dropbox
    Item list numbered from A to Z for items in stock
    reroll button

--BACKEND--
magic_item_shop class
    Function for new_magic_shop
        default random parameters location, shop_type, (location_description, shopkeeper), item_stock
            location will determine length of item_stock and chances for higher rarity items
            shop_type will determine the types of items that appear in item_stock

load in a list of random Items (most likely a CSV or JSON file of the items)

item_class 
    Function for new_magic_item
        name, type, attunement, rarity 
        class_restriction (if applicable), 
        description (if applicable), 
        book_location [book, pg #], price

--GENERATOR--
run new_magic_shop
Create a Variable magic_item_shop
Create a String Variable for location
Create a String Variable for shop_type
Create a String Variable for location_description
Create a String Variable for shop_description
Create a String Variable for shopkeeper
Create an empty list or dictionary for items
'''

from magic_item_shop import magic_item_shop

#initialization
magic_shop = magic_item_shop("Benny's Booming Bargains")
magic_shop_name = magic_shop.name
magic_shop_location = magic_shop.location
magic_shop_type = magic_shop.shop_type
# magic_shop_location_desc = magic_shop.location_description
# magic_shop_shop_desc = magic_shop.shop_description
# magic_shop_shopkeeper = magic_shop.shopkeeper
# magic_shop_stock_list = magic_shop.item_stock

print(magic_shop.__dict__)

