class Bankaccount:
    def __init__(self,accno,name,typeacc,balance):
        self.accno=accno
        self.name=name
        self.typeacc=typeacc
        self.balance=balance
    def deposit(self):
        amount=float(input("Enter the amount to be deposited:"))
        self.balance += amount
        print("\nAmount deposited:",amount)
        print("Current balance:",self.balance)
    def withdraw(self):
        amount=float(input("Enter the amount to be withdrawn:"))
        if self.balance>=amount:
            self.balance -= amount
            print("You withdrew:",amount)
            print("Current balance:",self.balance)
        else:
            print("\nInsufficient balance")
a=int(input("Enter your account number:"))
b=input("Enter your name:")
c=input("Enter your account type:")
account=Bankaccount(a,b,c,10000)
while(True):
    n=int(input(" 1 for deposit\n 2 for withdraw\n 0 for exit\n Enter your choice:\n"))
    print(n)
    if n==1:
        account.deposit()
    elif n==2:
        account.withdraw()
    elif n==0:
        break
    else:
        print("Invalid")
