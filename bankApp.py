import sqlite3

sqliteConnection = sqlite3.connect('sql.db')

class coustomer:
    def __init__(self, name, passWord ):
        self.name = name
        self.passWord = passWord

class bank(coustomer):
    def __init__(self, name, passWord, balance ,Amount):
        super().__init__(name, passWord)
        self.balance = balance
        self.Amount = Amount
  

def displayAccDetail():
    print("""             Account Details
              a) Amount Deposit
              b) Amount Withdrawal
              c) Check Balance
              d) Exit""")
    choice=input("")

def validate(custName,passWord):
    return True

def main():
    bal=amt=0
    
    print("""             Customer
                1. Customer Login
                2. New Customer Sign inc
                3. exit

          """)
    choice1 = int(input("Enter your choice"))
    if(choice1 == 1):
        print("Enter coustomer name")
        custName = input()
        print("Enter your Password")
        passWord = input()
        if(validate(custName,passWord)):
            print("welcome "+ custName)
        else:print("invalid user")
        
        
        bank(custName,passWord,bal,amt)
        
    if(choice1 == 2):
         print("Enter coustomer name")
         custName = input()
         print("Enter your Password")
         passWord = input()
         
         
         if(validate(custName,passWord)):
            print("welcome "+ custName)
         else:print("invalid user")
        
    
main() 
