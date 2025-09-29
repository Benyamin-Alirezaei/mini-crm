import random
import csv
import datetime
import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=".......",
    database="customer"
)
cursor = conn.cursor()

#Decorator

def time(func):
    """Decorator to print current time and minute before executing a function"""
    def wrapper(self):
        now = datetime.datetime.now()
        minute = now.minute
        print(f"current TIME:{now}")
        print(f"current MINUTE:{minute}")
        result = func(self)
        return result
    return wrapper

#Customer class
class Customer():
    """Initialize the Customer class with an empty list to store customer names"""
    def __init__(self):
     self.customer = []
    
    @time
    def add_customer(self):
        """Add a new customer to the internal list.Checks for duplicates before adding"""
        try:
            custome1 = str(input("plaese enter your custmer numbers:"))
            if custome1 not in self.customer:
             self.customer.append(custome1)
             print(f"Add:{self.customer}")
            else:
                print(f"custem already have been{self.customer}")
        except Exception as e:
            print("Dont wrong world again please!!")
    
    @time
    def show_customer(self):
        """Show all customers in the internal list.Applies a discount if current minute > 35"""
        now = datetime.datetime.now()
        minute = now.minute
        
        for cust in self.customer:
            print(f"customer:{cust}")
        if minute > 35:
            print(f"discount 40% for users:{self.customer}")
        else:
            print(f"NO DISCOUNT:{self.customer}")
        
            

        
    @time
    def save_csv(self):
        """Save all customers to a CSV file"""
        file_name_custmer = "customer.csv"
        with open (file_name_custmer,"w",newline="",encoding="utf-8") as file:
           try:
               write = csv.writer(file)
               write.writerow(["Customer"])
               for custom in self.customer:
                write.writerow([custom])
                print(f"save this file has name{file_name_custmer}")
           except Exception as e:
               print("Invalid input. Please try again")
   
    @time
    def delete_customer(self):
        """Delete a customer from the internal list by name"""
        try:
            customer1 = str(input("please enter your customer:"))
            for customer1 in self.customer:
              self.customer.remove(customer1)
            print(f"DELETE CUSTOMER{self.customer}")
        except Exception as e:
            print("invalid input. please try again!!!")
   
    @time
    def save_mysql(self):
        """Save all customers to MySQL database.Uses INSERT IGNORE to avoid duplicates"""
    def save_mysql(self):
        try:
            for cust in self.customer:
                cursor.execute("INSERT IGNORE INTO customers (name) VALUES (%s)", (cust,))
            conn.commit()
            print("All customers saved to MySQL!")
        except Exception as e:
            print(f"Error saving to MySQL: {e}")
            

               
#Main programe
ALL_CUSTOME = Customer()
while True:

    print("MENU")
    print("1:add_customer")
    print("2:show_customer")
    print("3:save_csv")
    print("4:delete_customer")
    print("5:save_mysql")
    print("6:EXIT")

    choice = str(input("please ADD numbers: (1-5):"))

    if choice == "1":
        ALL_CUSTOME.add_customer()
    elif choice == "2":
        ALL_CUSTOME.show_customer()
    elif  choice == "3":
        ALL_CUSTOME.save_csv()
    elif  choice == "4":
        ALL_CUSTOME.delete_customer()
    elif  choice == "5":
         ALL_CUSTOME.save_mysql()
         print("EXIT")
         break

#Close MySQL connection before exiting.

