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
