"""
class Bank to create account for users
"""
import uuid
import os

class Bank():

    def __init__(self):
        pass


    @staticmethod
    def create_random_account_number():
        account_number = str(uuid.uuid4().int >> 64)[0:9]
        return account_number

    @staticmethod
    def create_random_card_number():
        card_number = str(uuid.uuid4().int >> 64)[0:16]
        return card_number

    @staticmethod
    def add_to_accounts_file(account_number):
        f = open("Accounts.txt", "a+")
        f.write(str(account_number)+"\n")
        f.close

    @staticmethod
    def create_text_file_for_account(account_number,name,phone_number,id):
        with open(account_number+".txt","a+") as f:
            f.write("name : " + name + "\n")
            f.write("phone_number : "+phone_number + " \n")
            f.write("id : "+id + "\n")
            f.write("balance : "+"0" + "\n")
            os.fsync(f)
            f.close()



    def create_bank_account(self,name,phone_number,id):
        account_number = self.create_random_account_number()
        self.add_to_accounts_file(account_number)
        self.create_text_file_for_account(account_number,name,phone_number,id)
        return account_number

    def create_card_for_account(self,account_number):
        with open(account_number+".txt", "r+") as out_file:
            buf = out_file.readlines()
            out_file.seek(0)
            new_card = self.create_random_card_number()
            buf.insert(4,"card :"+new_card+"\n")
            out_file.writelines(buf)
            out_file.close()
        f = open(account_number+".txt", "a+")
        f.write(new_card + " : " + account_number + "\n")
        f.close


bank=Bank()
# bank.create_bank_account("ahmad", "12", "12")
bank.create_card_for_account("833896336")
# method returns value of balance from file of account
def get_balance(account_number):
    with open(account_number + ".txt", "r+") as out_file:
        buf = out_file.readlines()
        balance=buf[3] # pointer variable balance to place of value balance
        balance=balance[10:]# get the number without string 'balance :'
        out_file.close()
    return balance

value=get_balance("833896336")
print (value)
def upDate_balance(self,account_number):
        with open(account_number + ".txt", "wr+") as out_file:
            out_file.seek(0)
            buf = out_file.readlines()
            buf[3]="aaa"
            out_file.close()

upDate_balance("833896336")
