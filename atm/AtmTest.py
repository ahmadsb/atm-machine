from atm.BankCard import BankCard
from atm.Atm import Atm
import os
card_number = input("please enter your card number\n")
print("inserting card")
def authorized_access(account_number):
    atm_machine = Atm(account_number)
    option = input("what do you want to do"
                   "\n1-withdraw money "
                   "\n2-deposit money "
                   "\n3-transfer money"
                   " \n4-transition history")
    if option == "1":
        atm_machine.withdraw_money(account_number)
    elif option is "2":
        atm_machine.deposit_money(account_number)
account_number = Atm.check_if_card_exists(card_number)
if account_number == -1:
    print("card not found")
else:
    pin = input("please enter your pin\n")
    if Atm.check_if_pin_is_correct(account_number,card_number,pin)== 1:
        authorized_access(account_number)
    else:
        print("pin is wrong")


