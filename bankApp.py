import sqlite3      # Importing SQLite database module
try:   
  sqliteConnection = sqlite3.connect('bankDataBase.db')     # Establishing a connection with the database
  cursor = sqliteConnection.cursor()      # Creating a cursor object to traverse through the database
except sqlite3.Error as e:   # Catching an exception if there is any
    print("An error occurred while connecting to database:", e)
else:
    cursor.execute("create table IF NOT EXISTS bankDataBase (custName text, password text , balance integer);")     # To create table in Database


    class coustomer:    #class coustomer
        def __init__(self, name, passWord ):           # Initializing a customer with given parameters
            self.name=name;                          # Name of the user
            self.passWord=passWord;                # Password of the user   
           

    class bank(coustomer):                 # Inheritance from the 'customer' class
        def __init__(self, name, passWord, balance ):        # Overridden constructor for 'Bank' class
            super().__init__(name, passWord)    # Calling the parent constructor using 'super()'
            self.balance = balance     # Adding balance attribute in Bank class
        def displayAccDetail( self):    # Method to display account details
            print("""             Account Details       
                a) Amount Deposit
                b) Amount Withdrawal
                c) Check Balance
                d) Exit""")         # Printing the menu options
            choice=input("Enter your choice ")      # Taking input from the user
            if choice == 'a':
                self.deposit()
            elif choice == 'b':
                self.Withdrawal()
            elif  choice == 'c':
                self.checkBalance()
            else :
                print("invalid input")
                main()    
                
        def deposit(self):          # Function to handle deposit amount
            Amount = int(input("Enter the amount you want to deposite :"))   
            if(Amount >= 1):        # If the entered value is greater than or equal to one then only it will be inserted into
                qerry = ("select balance from bankDataBase where custname =? ;")    # To select balance from databse
                value = (self.name ,)           # Tuple containing values
                cursor.execute(qerry,value)     # Executing SQL query
                temp = cursor.fetchone()        # Fetching one record at a time
                Amount +=  temp[0]              # Updating the existing balance by adding the new amount
                updateQuery ="update bankDataBase set balance =? where custname=?"  #SQL Query to Update the data
                dataTuple=(Amount,self.name)            # Tuple containing values
                cursor.execute(updateQuery,dataTuple )  # Executing SQL query
                sqliteConnection.commit()               #  Commiting the changes
                print("Deposited sucessfully")
            else:print("Enter a valid amount")
            
            self.displayAccDetail()                     # Calling the method to display account detail again
                
            
        def Withdrawal(self):                           # Function to handle withdrawal amount
            Amount = int(input("Enter the amount you want to withdraw :"))   # Getting the withdrawal amount
            if(Amount > 0):     # If the entered amount is greater than zero then only it will be processed
                qerry = ("select balance from bankDataBase where custname =? ;")  # Query to get the current balance of the customer
                value = (self.name ,)          # Tuple containing values
                cursor.execute(qerry,value)    # Executing SQL Query
                temp = cursor.fetchone()       # Fetching one record at a time
                if Amount < temp[0]:           # Check if the  given amount is less than the available balance
                    Amount = temp[0] - Amount  # Subtract the  given amount from the existing balance
                    updateQuery ="update bankDataBase set balance =? where custname=?"  # Modifying the query with ? as placeholder and tuple of values
                    dataTuple=(Amount,self.name)                # Tuple containing values
                    cursor.execute(updateQuery,dataTuple )      # Executing SQL query
                    sqliteConnection.commit()                   # Committing the changes
                else:print("insifficinet balance")
            else:print("invalid input") 
            self.displayAccDetail()         # Displaying the account details again after processing the transaction
                
        def checkBalance(self):             # Method to check the current balance of an account holder
                qerry = ("select balance from bankDataBase where custname =? ;")    #
                value = (self.name ,)       # Tuple containing values
                cursor.execute(qerry,value)
                temp = cursor.fetchone()
                print(f"Your current Balance is {temp[0]}")
                self.displayAccDetail()             # Calling the method to display account details again
        

                
        

    def validate(custName,passWord): # Method the check if the name and password is exist in the database
        data = cursor.execute("select custName , passWord from bankDataBase;") # Select statement
        for x,y in data:        # Valiadting the coustomer details
            if(x==custName and y==passWord):        
                return(True)
# Main function which acts as the controller for our program
    def main():
        
        
        
        print("""             Customer
                    1. Customer Login
                    2. New Customer Sign inc
                    3. exit

            """) # Displaying options to user
        choice1 = input("Enter your choice  ") #Taking user input
        if(choice1 == '1'):
            print("Enter coustomer name  ")
            custName = input()
            print("Enter your Password  ")
            passWord = input()
            if(validate(custName,passWord)): # calling the validate ()
                print("welcome "+ custName) 
                qerry = ("select balance from bankDataBase where custname = ? ;")  # Query to get customer's detail
                value = (custName,) # passing customer name as a tuple
                cursor.execute(qerry,value)        # Executing select query with passed argument
                data = cursor.fetchone()           # Fetching one record at a time
                balance=data[0]                    # Assigning balance to variable balance
                bankobj = bank(custName,passWord,balance) # Creating bank object
                bankobj.displayAccDetail()      #Calling the display()
                
            else:
                print("invalid user")
                main()

            
            
            
        if(choice1 == '2'): # User SignIn
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
    main()  # Calling the main  function again and again till user enters correct option
    cursor.close() # Closing the coursor
    sqliteConnection.commit() # commiting the transaction
    sqliteConnection.close() #  closing the connection