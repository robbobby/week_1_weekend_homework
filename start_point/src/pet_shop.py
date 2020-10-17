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

                            ##### Question 7 #####
def get_stock_count(pet_shop_list):
    return len(pet_shop_list["pets"])

                            ##### Question 8 #####
                            ##### Question 9 #####
def get_pets_by_breed(pet_shop_list, breed_name):
    pet_list = []
    for pet in pet_shop_list["pets"]:
        if pet["breed"] == breed_name:
            pet_list.append(pet["name"])
    return pet_list
                            ##### Question 10 #####
                            ##### Question 11 #####
def find_pet_by_name(pet_shop_list, pet_name):
    for pet in pet_shop_list["pets"]:
        if pet["name"] == pet_name:
            return pet

                            ##### Question 12 #####
def remove_pet_by_name(pet_shop_list, name_to_remove):
    for pet in pet_shop_list["pets"]:
        if pet["name"] == name_to_remove:
            pet_shop_list["pets"].remove(pet)
                     
                            ##### Question 13 #####
def add_pet_to_stock(pet_shop_list, new_pet):
    pet_shop_list["pets"].append(new_pet)

                            ##### Question 14 #####
def get_customer_cash(customer):
    return customer["cash"]

                            ##### Question 15 #####
def remove_customer_cash(customer, cash_gone):
    customer["cash"] -= cash_gone

                            ##### Question 16 #####

def get_customer_pet_count(customer):
    return len(customer["pets"])

                            ##### Question 17 #####
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

                            ##### Question 18 #####
                            ##### Question 19 #####
                            ##### Question 20 #####
def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop_list, pet, customer):
    try:
        if customer_can_afford_pet(customer, pet) and find_pet_by_name(pet_shop_list, pet["name"]):
            remove_customer_cash(customer, pet["price"])
            add_pet_to_customer(customer, pet)

            # if (type(pet) == "list"):
            #     increase_pets_sold(pet_shop_list, len(pet))
            # else:
            
            increase_pets_sold(pet_shop_list, 1)
            remove_pet_by_name(pet_shop_list, pet["name"])
            add_or_remove_cash(pet_shop_list, pet["price"])
    except:
        return