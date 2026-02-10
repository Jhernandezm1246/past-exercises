#Create a class Product 
#with Name, price and amount 
#Create a class inventory that 
#Saves products on a list 
#Has methods for adding a product, show all products, calculate total value of the inventory 

class Product():

    def __init__(self,name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


class Inventory():

    def __init__(self):
        self.inventory_of_products = []

    def adding_a_product(self, new_product):
        self.inventory_of_products.append(new_product)

    def show_all_products(self):

        for product in self.inventory_of_products:
            print(f"The product name: {product.name} Product price: {product.price} Product amount: {product.amount}")


    def calculate_total_inventory_value(self):

        total_value = 0

        for product in self.inventory_of_products:

            new_value = product.price * product.amount 

            total_value += new_value

        return total_value
    

    

def new_product(inventory):

    production_chain = input("How many products you like to add: ")


    if production_chain.isdigit() == False:
        while production_chain.isdigit() == False:
            print("Please only type numbers")
            production_chain = input("Type the product price: ")
            if production_chain.isdigit() == True:
                break 

    counter = 0

    while counter < int(production_chain):

        name = input("Type the name of the product: ")
        while True:
            if any(letter.isdigit() for letter in name):
                print("Name should only have letter: ")
                continue
            else:
                break

        
        while True:
            price = input("Type the product price: ")

            try:
                price = float(price)

            except ValueError as error:
                print(f"Error [ValueError] Please note that at this point you should only add numbers")
                print("Please try again")
                continue
            
            if float(price) != ValueError:
                break

        """if price.isdigit() == False:
            while price.isdigit() == False:
                print("Please only type numbers")
                price = input("Type the product price: ")
                if price.isdigit() == True:
                    break """

        amount = input("Type the product amount: ")
        if amount.isdigit() == False:
            while amount.isdigit() == False:
                print("Please only type numbers")
                amount = input("Type the product amount: ")
                if amount.isdigit() == True:
                    break 

        new_product_addition = Product(name, float(price), int(amount))

        inventory.adding_a_product(new_product_addition)
        

        counter += 1 

    
    

new_inventory = Inventory()



system_start = str(input("Would you like to start the program (Y/N): ").upper()) 

while system_start != "Y" and system_start != "N": 
    print("Please note that at this moment you should only select Y or N ") 
    system_start = str(input("Would you like to start the program (Y/N): ").upper())


print("-------------------------------------------------")
print("1.Add a new product: ")
print("2.Show all products in inventory: ")
print("3.Show total value of inventory: ")
print("-------------------------------------------------")



def menu_selection():
    menu_selection = input("Select one of the options above: ")

    if menu_selection.isdigit() == False:
        while menu_selection.isdigit() ==False:
            print("Please only select one of the numbers above")
            menu_selection = input("Select one of the options above: ")
            if int(menu_selection).isdigit() and int(menu_selection) == 1 or int(menu_selection) == 2 or int(menu_selection) == 3:
                
                break
                
    return int(menu_selection)




while system_start == "Y":
    new_system_run = menu_selection()

    if new_system_run == 1:

        new_product(new_inventory)

    elif new_system_run == 2:

        new_inventory.show_all_products()

    elif new_system_run == 3:

        total_value = new_inventory.calculate_total_inventory_value()

        if total_value == 0:
            print("Total Inventory value is 0")

        else:
            print(f"Total inventory value is {total_value}")

    system_start = str(input("Would you like to continue (Y/N)").upper())

    