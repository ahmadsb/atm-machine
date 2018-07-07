from os.path import exists
class Atm:

    def __init__(self,account_number):
        self.account_number = account_number

    def insert_card(self,card):
        print("inserting card")

    def withdraw_money(self, account_number):
        if(exists("account_number.txt")):
            value = input("Please, Enter value to withdraw money:")
            value = int(value)
            # get value of balance
            balance=1000 #f.g 1000
            if( balance >= value):
                balance=balance-value
                #upDate_balance(balance)
            else:
                print("Sorry, not fount money !!")
        else:
            print("Please, try again number account not found")

    def deposit_money(self,account_number):
        if (exists("account_number.txt")):
            value = input("Please, Enter value to deposit money:")
            value = int(value)
            #get value of balance
            balance=balance+value
            #upDate_balance(balance)
        else:
            print("Please, try again number account not found")

    def transition_history(self,account):
        print("printing transition history")






