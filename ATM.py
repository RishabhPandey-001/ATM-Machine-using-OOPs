# ATM machine using Object oriented programming 
class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
            Hi How can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Anything else to exit  
            """)    
        
        if user_input == '1':
            self.create_pin()

        elif user_input == '2':
            self.change_pin()
            
        elif user_input == '3':
            self.chechk_balance()
           
        elif user_input == '4':
            self.withdrawl()
            
        else:
            exit()  

    def create_pin(self):
        user_pin = (input("Enter your pin: "))
        self.pin = user_pin

        user_balance = int(input("Enter your balance: "))
        self.balance = user_balance

        print("PIN created successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter old PIN: ")    
        if old_pin == self.pin:
         new_pin = input("Enter New PIN: ")
         self.pin = new_pin
         print("PIN chnage successfully")
         self.menu()
        else:
           print("You have entered the wrong PIN")
           self.menu()          

    def chechk_balance(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            print(f"Your available balance is {self.balance}")
        else:
            print("You have entered the wrong PIN")    
        self.menu()    

    def withdrawl(self):
          user_pin = input("Enter your PIN: ")
          if user_pin == self.pin:
            Amount = int(input("Enter the amount you want to withdrwal: "))
            if Amount<= self.balance:
              self.balance = self.balance - Amount
              print(f"You have withdrawn ₹{Amount} successfully!")
            else: 
              print("SORRY, You do not have enough balance ") 
          else:
              print("Opps, You have entered the wrong PIN")     
          self.menu()

obj = Atm()

