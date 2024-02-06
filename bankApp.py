import sqlite3

sqliteConnection = sqlite3.connect('bankDataBase.db')
cursor = sqliteConnection.cursor() 
cursor.execute("create table IF NOT EXISTS bankDataBase (custName text, password text , balance integer);") 


class coustomer:    
    def __init__(self, name, passWord ):
        self.name = name
        self.passWord = passWord

class bank(coustomer):
    def __init__(self, name, passWord, balance ):
        super().__init__(name, passWord)
        self.balance = balance
    def displayAccDetail( self):
         print("""             Account Details
              a) Amount Deposit
              b) Amount Withdrawal
              c) Check Balance
              d) Exit""")
         choice=input("Enter your choice ")
         if choice == 'a':
           self.deposit()
         elif choice == 'b':
             self.Withdrawal()
         elif  choice=='c':
            self.checkBalance()
         else :
             print("invalid input")
             main()    
              
    def deposit(self):
       Amount = int(input("Enter the amount you want to deposite :"))   
       if(Amount >= 1):
            print('hs')
            qerry = ("select balance from bankDataBase where custname =? ;")  
            value = (self.name ,)
            cursor.execute(qerry,value)
            temp = cursor.fetchone()
            Amount +=  temp[0]
            updateQuery ="update bankDataBase set balance =? where custname=?"
            dataTuple=(Amount,self.name)
            cursor.execute(updateQuery,dataTuple )
            sqliteConnection.commit()
            
       else:print("Enter a valid amount")
         
       self.displayAccDetail()   
            
        
    def Withdrawal(self):
        Amount = int(input("Enter the amount you want to withdraw :"))   
        if(Amount > 0):
            qerry = ("select balance from bankDataBase where custname =? ;")  
            value = (self.name ,)
            cursor.execute(qerry,value)
            temp = cursor.fetchone()
            if Amount < temp[0]:
                Amount = temp[0] - Amount
                updateQuery ="update bankDataBase set balance =? where custname=?"
                dataTuple=(Amount,self.name)
                cursor.execute(updateQuery,dataTuple )
                sqliteConnection.commit()
            else:print("insifficinet balance")
        else:print("invalid input") 
        self.displayAccDetail()
               
    def checkBalance(self):
            qerry = ("select balance from bankDataBase where custname =? ;")  
            value = (self.name ,)
            cursor.execute(qerry,value)
            temp = cursor.fetchone()
            print(f"Your current Balance is {temp[0]}")
    

def validate(custName,passWord):
    data = cursor.execute("select custName , passWord from bankDataBase;")
    for x,y in data:
        if(x==custName and y==passWord):
            return(True)

def main():
    
    
    
    print("""             Customer
                1. Customer Login
                2. New Customer Sign inc
                3. exit

          """)
    choice1 = input("Enter your choice  ")
    if(choice1 == '1'):
        print("Enter coustomer name  ")
        custName = input()
        print("Enter your Password  ")
        passWord = input()
        if(validate(custName,passWord)):
            print("welcome "+ custName)
            qerry = ("select balance from bankDataBase where custname = ? ;")  
            value = (custName,)
            cursor.execute(qerry,value)
            data = cursor.fetchone()
            balance=data[0]
            bankobj = bank(custName,passWord,balance)
            bankobj.displayAccDetail()
            
        else:
            print("invalid user")
            main()

        
        
        
    if(choice1 == '2'):
         print("Enter coustomer name  ")
         custName = input()
         print("Enter your Password  ")
         passWord = input()
         sql_query = "INSERT INTO bankDataBase (custName , password , balance) VALUES (?, ?, ?)"
         values = (custName,passWord,0)
         cursor.execute(sql_query, values)
         sqliteConnection.commit()
         if(validate(custName,passWord)):
            print("welcome "+ custName)
         else:
             print("invalid user")
         main()
    else:
        print("invalid input")
        main()  
main() 
