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

            with open("../accounts/" + account_number + ".txt", "r+") as f:
                balance=1000     # get value of balance
                os.fsync(f)

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

            #steps 1. get balance from account file
            #      2. do sum on balance
            #      3. upDate balance in account file

            value = int(value) # convert from str to int
            balance = get_balance(account_number)  # get value balance in type str
            balance = int(balance)# convert from str to int
            new_balance=balance+value
            upDate_balance(account_number, new_balance)
        else:
            print("Please, try again number account not found")

    def transition_history(self,account):
        print("printing transition history")

    @staticmethod
    def get_balance(self, account_number):
        with open(account_number + ".txt", "r+") as out_file:
            buf = out_file.readlines()
            balance = buf[3]  # pointer variable balance to place of value balance
            balance = balance[10:]  # get the number without string 'balance :'
            out_file.close()
        return balance

    @staticmethod
    def upDate_balance(self,account_number, new_balance):
        with open(account_number + ".txt", "w+") as out_file:
            buf = out_file.readlines()
            buf[3]="balance : "+new_balance
            out_file.close()





