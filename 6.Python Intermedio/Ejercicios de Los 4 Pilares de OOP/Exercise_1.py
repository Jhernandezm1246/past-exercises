#Exercise 1
#Create a class Bank Account that has
#Attribute balance 
#Has a method insert money
#has a method to withdraw money 
#Create another class inherit from this one called SavingsAccount that 
#Has attribute my balance that can be assigned once created 
#Show an error if at the moment of trying to withdraw money the balance end up being below of my balance 
#Meaning that you can withdraw money only when the balance stay above or my balance 

from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self):
        self.balance = 0 


    def insert_money(self):
        
        while True:
            amount = input("Type the amount you like to insert: ")

            try:
                amount = float(amount)

                if amount < 0:
                    print("The amount can not be negative please try again") 

                else:
                    self.balance += amount
                    break

            except ValueError as error:
                print(f"Error [ValuerError] Please only use numbers")
                print("Please try again")
        

    @abstractmethod
    def withdraw_money(self):

        pass

    def show_balance(self):

        print(f"Your Balance is {self.balance}")

        
class SavingsAccount(BankAccount):

    

    def __init__(self):

        super().__init__()
        

        while True:
            self.min_balance = input("Type the min balance to withdraw from your account: ")

            try:
                self.min_balance = float(self.min_balance)

                if self.min_balance < 0:
                    print("The amount can not be negative please try again") 

                else:
                    break

            except ValueError as error:
                print(f"Error [ValuerError] Please only use numbers")
                print("Please try again")


    def withdraw_money(self):

        

        while True:
            subtract = input("Type the amount you like to insert: ")

            try:
                subtract = float(subtract)

                if subtract < 0 :
                    print("The amount can not be negative please try again") 

                else:

                    if subtract < self.min_balance and subtract <= self.balance:
                        print(f"You are not allowed to subtract less than {self.min_balance}")

                    else:

                        self.balance -= subtract
                        break

            except ValueError as error:
                print(f"Error [ValuerError] Please only use numbers")
                print("Please try again")


system_start = str(input("Would you like to start the program (Y/N): ").upper()) 

while system_start != "Y" and system_start != "N": 
    print("Please note that at this moment you should only select Y or N ") 
    system_start = str(input("Would you like to start the program (Y/N): ").upper())



new_account = SavingsAccount()


print("ATM Machine")
print("--------------")
print("1.Add Funds")
print("2.Withdraw Funds")
print("3.Show Funds")
print("--------------")


def menu_selection():
    menu_selection = input("Select one of the options above:")

    while True:
        try:
            menu_selection = int(menu_selection)

            if menu_selection != 1 and menu_selection != 2 and menu_selection != 3:
                print("Invalid option please try again")
            
            else:
                
                return menu_selection

        except ValueError as error:
            print(f"Error [ValueError] Please note you should only add numbers please try again")

            

    

while system_start == "Y":

    new_system_run = menu_selection()


    if new_system_run == 1:
        new_account.insert_money()

    if new_system_run == 2:
        new_account.withdraw_money()

    if new_system_run == 3:
        new_account.show_balance()