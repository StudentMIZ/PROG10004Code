from account import Account

class Atm:
    def __init__(self):
        self.screen = True                          #This refers to if the screen is working
        self.keypad = True                          #This refers to the condition of the keypad
        self.cashDispen = True                      #This means that there is enough amount
        self.depositSlot = True                     #The slot has no issues
        self.cash = 10000
        self.city = "Toronto"
        self.province = "Ontario"
        self.postalCode = "TTTTTT"


    def disAccountInfo(self, account1):
        print(account1.firstName)
        print(account1.lastName)
        print(account1.chequeBalance)
        print(account1.savingBalance)