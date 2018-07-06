"""
class Bank to create account for users
"""
import uuid


def createNumAccount():
    numAccounts = str(uuid.uuid4().int >> 64)[0:8] + str(uuid.uuid4().int >> 64)[0:8]
    return numAccounts

def writeNumAccountInFile(numAccount):
    f = open("Accounts.txt", "a+")
    f.write(str(numAccount)+"\n")
    f.close

number=createNumAccount();
writeNumAccountInFile(number)

# class Bank:
#
#     def __init__(self):
#         pass
#
#     def createAccount(self):
#         numAccounts=str(uuid.uuid4().int>>64)[0:8] + str(uuid.uuid4().int>>64)[0:8]
#         print (numAccounts)
