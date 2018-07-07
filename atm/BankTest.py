from atm.Bank import Bank

bank = Bank()
while(True):
    option = input("welcome to bank please pick a number \n 1-create new account \n 2-create new card\n 3-exit")
    if option == "1":
        name = input("please enter your name\n")
        number = input("please enter your number\n")
        id = input("please enter your id\n")
        account_number=bank.create_bank_account(name,number,id)
        print("account successfully created account number is "+account_number)
    elif option == "2":
        account_number = input("please enter your account_number")
        bank.create_card_for_account(account_number)
    elif option == "3":
        break
    else:
        print("please enter correct number")
