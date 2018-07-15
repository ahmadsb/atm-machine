from os.path import exists
import os
class Atm:
    def __init__(self,account_number):
        self.account_number = account_number

    def insert_card(self,card):
        print("inserting card")

    def withdraw_money(self, account_number):
        if(exists("../accounts/"+account_number+".txt")):

            value = input("Please, Enter value to withdraw money:")
            value = int(value)

            with open("../accounts/" + account_number + ".txt", "r+") as f:
                balance=self.get_balance(account_number)
                balance=int(balance)
                os.fsync(f)

            if( balance >= value):
                new_balance=balance-value
                self.upDate_balance(account_number, str(new_balance))

                lines = []
                file = open("../accounts/" + account_number + ".txt")
                with file:
                    for line in file:
                        lines.append(line)
                lines.append("successfully withdraw money: "+str(value)+" and current balance : "+str(new_balance)+"\n")
                print(lines)
                file = open("../accounts/" + account_number + ".txt", "w+")
                for item in lines:
                    file.write("%s" % item)
                file.close()

            else:
                print("Sorry, not found money !!")
        else:
            print("Please, try again number account not found")
            return -1
    def append_transition(self,account_number,type,value):

        return
    def deposit_money(self,account_number):

        if (exists("../accounts/"+account_number+".txt")):
            value_deposit = input("Please, Enter value to deposit money:")
            value_deposit = int(value_deposit)
            old_blanace = self.get_balance(account_number)
            new_balance = int(old_blanace) + value_deposit
            self.upDate_balance(account_number, new_balance)
            self.append_transition(account_number,"deposit",value_deposit)
            print (" successfully deposit money ")

            lines=[]
            file = open("../accounts/" + account_number + ".txt")
            with file:
                for line in file:
                    lines.append(line)
            lines.append("successfully deposit money: " + str(value_deposit) + " and current balance : " + str(new_balance)+"\n")
            print(lines)
            file = open("../accounts/" + account_number + ".txt", "w+")
            for item in lines:
                file.write("%s" % item)
            file.close()
        else:
            print("Please, try again number account not found")

    def transition_history(self,account):
        if (exists("../accounts/"+account+".txt")):
            value_tran = input("Please, Enter value to transition :")
            value_tran = int(value_tran)

            self.upDate_balance_transition(account, value_tran)
        else:
            print ("file not found")




    # method returns value of current balance in account
    # that help method uses to upDate_balance
    @staticmethod
    def get_balance(account_number):
        with open("../accounts/"+account_number + ".txt", "r+") as out_file:
            buf = out_file.readlines()
            balance=buf[3] # pointer variable balance to place of value balance
            balance=balance[10:]# get the number without string 'balance :'
            out_file.close()
        return balance

    # method upDates value balance in account

    def upDate_balance(self,account_number, new_balance):
        lines=[]
        old_balance=self.get_balance(account_number)
        file=open("../accounts/"+account_number+".txt", "r+")
        with file:
            for line in file:
                if 'balance : ' in line:
                    line= line.replace("balance : "+str(old_balance),"balance : "+str(new_balance)+"\n")
                lines.append(line)
        file=open("../accounts/"+account_number+".txt", "w+")
        for item in lines:
            file.write("%s" % item)
        file.close()


    def transfer_money(self,account_number,account_other, amount):
        lines = []
        if (self.check_balance(account_number, amount) != -1 and exists("../accounts/" + account_other + ".txt")):
                old_balance = self.get_balance(account_other)
                old_balance=int(old_balance)# casting to int
                new_balance=old_balance+int(amount)



                file = open("../accounts/" + account_other + ".txt")
                with file:
                    for line in file:
                        if 'balance : ' in line:
                            line = line.replace("balance : " + str(old_balance), "balance : " + str(new_balance) + "\n")
                        lines.append(line)
                lines.append("from "+account_number+" transition: "+str(amount)+"and current balance : "+str(new_balance)+"\n")
                print(lines)
                file = open("../accounts/" + account_other + ".txt", "w+")
                for item in lines:
                    file.write("%s" % item)
                file.close()
        else:
            print("not enter")

    @staticmethod
    def check_if_card_exists(card_number):
        dictCorrect = {}
        if exists("../refrence/cards.txt"):

            with open('../refrence/cards.txt', 'r') as accounts:
                for line in accounts:
                    card_numbers,account_numbers = line.split(' : ')
                    print(card_numbers)
                    dictCorrect[card_numbers.strip()] = account_numbers.strip()
        try:

            return dictCorrect[card_number]
        except FileExistsError:
            return -1
    @staticmethod
    def check_if_pin_is_correct(account_number,card_number,pin):
        credit_cards = {}
        with open("../accounts/"+account_number+".txt","r") as account:
            for line in account:
                print(line[0:3])
                if line[0:4] == "card":
                    card_name,card_numbers,card_pin = line.split(" : ")
                    credit_cards[card_numbers] = card_pin
            print(credit_cards)
            if credit_cards[card_number].replace("\n","")==pin:
                return 1
            else:
                return -1

    def check_balance(self, account_number, amount):
        if (exists("../accounts/" + account_number + ".txt")):
            amount = int(amount)
            balance = self.get_balance(account_number)
            balance = int(balance)
            if (balance >= amount):
                new_balance = balance - amount
                self.upDate_balance(account_number, str(new_balance))

                lines = []
                file = open("../accounts/" + account_number + ".txt")
                with file:
                    for line in file:
                        lines.append(line)
                lines.append("successfully withdraw money: " + str(amount) + " and current balance : " + str(new_balance)+"\n")
                print(lines)
                file = open("../accounts/" + account_number + ".txt", "w+")
                for item in lines:
                    file.write("%s" % item)
                file.close()

                return new_balance

            else:
                print("Sorry, not found enough money !!")
                return -1
        else:
            print("Please, try again number account not found")
            return -1
