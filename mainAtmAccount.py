from atm import Atm
from account import Account

atmMachine1 = Atm()                             
account1 = Account()

account1.firstName = "John"
account1.lastName = "Rajeev"
account1.chequeBalance = 500
account1.savingBalance = 200

atmMachine1.disAccountInfo(account1)

