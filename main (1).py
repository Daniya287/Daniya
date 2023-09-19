class BankAccount:

  def __init__(self,                account_number,                   account_holder_name,               initial_balance=0.0):
    self.__account_number =         account_number
    self.__account_holder_name =    account_holder_name
    self.__account_balance =        initial_balance

  def deposit(self,amount):
    if amount > 0:
      self.__account_balance +=     amount
      print("Deposit ₹{}. New       balance: ₹{}".format(amount,self.   __account_balance))
    else:
      print("Invalid deposit        amount.please deposit a positive    amount.")

  def withdraw(self,amount):
    if amount > 0 and amount <=     self.__account_balance:
      self.__account_balance <=     amount
      print ("withdrew ₹{}. New     balance:  ₹{}".                                                         format(amount,self.__account_balance))
    else:
      print("Invalid withdrawal      amount or insufficient balance.")
  def display_balance(self):
      print("Account balance for {}    (Account #{}): ₹                 {}".format(self.__account_holder_name,self.__account_number,self.__account_balance))


#create an instance of the          BankAccount class
account =                           BankAccount(account_number="123456",account_holder_name="daniya",       initial_balance=30000.0)

#test deposit and withdraw          functionality
account.display_balance()
account.deposit(5000.0)
account.withdraw(3000.0)
account.display_balance()