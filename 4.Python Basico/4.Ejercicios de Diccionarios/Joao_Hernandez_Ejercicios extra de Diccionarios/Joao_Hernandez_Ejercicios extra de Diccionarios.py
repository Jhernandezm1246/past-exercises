#Excercise 1 

#Given a list of sales with the following information date, customer_email, items 
#And each item having the following information name, upc , unit_price 

#Create a dictionary that saves all the total sales from each UPC
"""

def excercise_one():


    geo_sales = [
        {
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
    ]


    try:

        new_selection = str(input("Would you like to add a new record? (Y/N)").upper())   
    
    except ValueError as error:
        print(f"Error [ValueError] Please make sure you are selection only Y or N")

    


    def new_entry(cycle):

        dic_sales = []

        counter = 0

        print("Please include the date and client information")

        new_sale = {
            "date": input("Add the date: "),
            "customer_email": input("Add the customer email: "),
            "items":[]

        }

        while counter < cycle:

            
            item_name = str(input("Add the item name: "))
            upc = str(input("Add the item upc: "))
            unit_price = float(input("Add the unit price: "))

            
            new_sale["items"].append({"name":item_name,"upc":upc,"unit_price":unit_price})
            counter += 1

        dic_sales.append(new_sale)
            
        print(dic_sales)
        return dic_sales    
                
    while new_selection == "Y":
        try:
            
            cycle = int(input("How many records you like to add to the list sales? "))
            geo_sales.append(new_entry(cycle))
            new_selection = str(input("Would you like to add a new record? (Y/N)").upper())   

        except ValueError as error:
            print(f"Error [ValueError] Please note at this point you should only select a number ")

    print(geo_sales)

    def total_upc(geo_sales):

        total_sales = {}

        for sale in geo_sales:
            for item in sale["items"]:
                upc = item["upc"]
                price = item["unit_price"]

                if upc not in total_sales:
                    total_sales[upc] = {
                        "name":item["name"],
                        "total":0,
                        "count":0
                    }
                total_sales[upc]["total"] += price
                total_sales[upc]["count"] += 1
                
        print("New Dictionary has the following records")
        print(total_sales)
        return total_sales

                
            



    total_upc(geo_sales)

excercise_one()


#Excercise 2 

#Given a list of sales with the following information NAME, EMAIL AND DEPERTMENT
#Create a dictionary that group employees by their department 

def excercise_two():


    employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]


    try:
        program_start = str(input("Would you like to add a new employee (Y/N)").upper())

    except ValueError as error:
        print(f"Error [ValueError] you entered an incorrect value")


    def new_entry(selection):
        try:
            if selection == "Y":
                cycle = int(input("How many records you like to add: "))
                return cycle
            
            else:
                print("Thanks for using the program")
                return 0

        except ValueError as error:
            print(f"Error [ValueError] you entered an incorrect value")



    cycle = new_entry(program_start)



    def new_employee(cycle):

        counter = 0

        new_employee = []
        
        while counter < cycle:

            name = str(input("Type the eployee name: "))
            email = str(input("Type the eployee email: "))
            department = str(input("Type the eployee department: "))

            new_employee.append({
                "name": name,
                "email": email,
                "department": department

            })
            counter += 1

        return new_employee
    


    def eployee_by_department(empoyees):

        department_dic = {}

        for employee in employees:
            dept = employee["department"]

            if dept not in department_dic:
                department_dic[dept] = {
                    "employees": [],
                    "count": 0
                }

            department_dic[dept]["employees"].append({
                "name": employee["name"],
                "email": employee["email"]
            })

            department_dic[dept]["count"] += 1


        print(department_dic)
        return department_dic

    adition_employee = new_employee(cycle)

    employees.extend(adition_employee)

    eployee_by_department(employees)


excercise_two()



#Excercise 3

#Given a list of sale products where each have a category and price 
#Create a dictionary that acumulate the total by category
"""
def excercise_three():

    products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

    try:


        selection = str(input("Would you like to add a new product ? (Y/N) ").upper())

    except ValueError as error:
        print(f"Error [ValueError] you selected the incorrect value please make sure only to select (Y or N)")

    def new_entry(selection):
        try:
            if selection == "Y":
                cycle = int(input("How many records you like to add: "))
                return cycle
            
            else:
                print("Thanks for using the program")
                return 0

        except ValueError as error:
            print(f"Error [ValueError] you entered an incorrect value")



    

    def new_product(cycle):

        counter = 0

        new_product = []
        
        while counter < cycle:

            name = str(input("Type the product name: "))
            category = str(input("Type the product category: "))
            price = float(input("Type the product price: "))

            new_product.append({
                "name": name,
                "category": category,
                "price": price

            })
            counter += 1

        return new_product


    def tota_sales_by_department(products):


        total_sale_by_dep = {}

        for product in products:
            
            
            prod = product["category"]
            price = product["price"]

            if prod not in total_sale_by_dep:
                total_sale_by_dep[prod] = {
                        "category":product["category"],
                        "total":0,
                        "count":0
                    }
            total_sale_by_dep[prod]["total"] += price
            total_sale_by_dep[prod]["count"] += 1

        return print(total_sale_by_dep)


    cycle = new_entry(selection)

    adition_product = new_product(cycle)

    products.extend(adition_product)

    tota_sales_by_department(products)


excercise_three()

