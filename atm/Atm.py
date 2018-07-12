from os.path import exists
class Atm:

    def __init__(self,account_number):
        self.account_number = account_number

    def insert_card(self,card):
        print("inserting card")

    def withdraw_money(self, account_number):
        if(exists(account_number+".txt")):
            value = input("Please, Enter value to withdraw money:")
            value = int(value)

            with open("../accounts/" + account_number + ".txt", "r+") as f:
                balance=get_balance(account_number)
                balance=int(balance)
                os.fsync(f)

            if( balance >= value):
                new_balance=balance-value
                upDate_balance(account_number, str(new_balance))
                print (" successfully withdraw money ")
            else:
                print("Sorry, not found money !!")
        else:
            print("Please, try again number account not found")

    def deposit_money(self,account_number):

        if (exists(account_number+".txt")):
            value_deposit = input("Please, Enter value to deposit money:")
            value_deposit = int(value_deposit)

            upDate_balance(account_number, value_deposit)
            print (" successfully deposit money ")
        else:
            print("Please, try again number account not found")

    def transition_history(self,account):
        if (exists(account+".txt")):
            value_tran = input("Please, Enter value to transition :")
            value_tran = int(value_tran)

            upDate_balance_transition(account, value_tran)
        else:
            print ("file not found")




    # method returns value of current balance in account
    # that help method uses to upDate_balance
    @staticmethod
    def get_balance(account_number):
        with open(account_number + ".txt", "r+") as out_file:
            buf = out_file.readlines()
            balance=buf[3] # pointer variable balance to place of value balance
            balance=balance[10:]# get the number without string 'balance :'
            out_file.close()
        return balance

    # method upDates value balance in account
    @staticmethod
    def upDate_balance(account_number, new_balance):
        lines=[]
        old_balance=get_balance(account_number)
        file=open(account_number+".txt", "r+")
        with file:
            for line in file:
                if 'balance : ' in line:
                  line= line.replace("balance : "+old_balance,"balance : "+new_balance+"\n")
                lines.append(line)
        file=open(account_number+".txt", "w+")
        for item in lines:
            file.write("%s" % item)
        file.close()

    @staticmethod
    def upDate_balance_transition(account_number,account, value_tran):
        lines = []
        old_balance = get_balance(account_number)
        old_balance=int(old_balance)# casting to int
        new_balance=old_balance+int(value_tran)

        file = open(account + ".txt", "r+")
        with file:
            for line in file:
                if 'balance : ' in line:
                    line = line.replace("balance : " + old_balance, "balance : " + new_balance + "\n")
                lines.append(line)
        lines.append("from"+account_number+"transition: "+int(value_tran))
        file = open(account_number + ".txt", "w+")
        for item in lines:
            file.write("%s" % item)
        file.close()


