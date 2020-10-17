# WRITE YOUR FUNCTIONS HERE

                            ##### Question 1 #####
def get_pet_shop_name(pet_shop_list):
    return pet_shop_list["name"]

                            ##### Question 2 #####
def get_total_cash(pet_shop_list):
    return pet_shop_list["admin"]["total_cash"]

                            ##### Question 3 #####
                            ##### Question 4 #####
def add_or_remove_cash(pet_shop_list, value_to_add):
    pet_shop_list["admin"]["total_cash"] += value_to_add

                            ##### Question 5 #####
def get_pets_sold(pet_shop_list):
    return pet_shop_list["admin"]["pets_sold"]

                            ##### Question 6 #####
def increase_pets_sold(pet_shop_list, number_of_pets_sold):
    pet_shop_list["admin"]["pets_sold"] += number_of_pets_sold

def get_stock_count(pet_shop_list):
    return len(pet_shop_list["pets"])

def get_pets_by_breed(pet_shop_list, breed_name):
    pet_list = []
    for pet in pet_shop_list["pets"]
        if pet["pet_type"] == breed_name
        pet_list.append(pet["name"])
    return pet_list.__len__