class BankAccount: 
       def __init__(self,account_number,holder_name,pin,balance=0):
              self.account_number=account_number
              self.holder_name=holder_name
              self.pin=pin
              self.balance=balance
              self.transactions=[]
       def verify_pin(self,entered_pin):
              return entered_pin==self.verify_pin

       def deposit(self,amount):
              if amount>0:
                     self.balance+=amount
                     self.transactions.append(f"Deposited: {amount}")
                     print(f"{amount}sucessfully deposited!")
                     
              else:
                     print("invalid amount!")

       def withdraw(self,amount):
           if 0<amount<=self.balance:
                   self.balance-=amount
                   self.transactions.append(f"withdrawn:{amount}")
                   print(f"{amount} sucessfully witdrawn!")
           else: 
                  print("invalid amount or insufficient funds!") 
       def check_balance(self):
        print("current_balance:{}".format(self.balance))


       def show_transactions(self):
        print("\n----mini statement-----") 
        for item in self.transactions:
                   print(item)

user1=BankAccount("12345", "sanjeev", "1234", 5000)
user1.verify_pin("1234")
user1.check_balance()
user1.deposit(1000)
user1.withdraw(2000)
user1.show_transactions()