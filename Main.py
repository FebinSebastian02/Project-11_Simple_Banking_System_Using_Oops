#Parent Class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def displayDetails(self):
        print("User Details\n")
        print("Name:- " + self.name)
        print("Age:- " + str(self.age))
        print("Gender:- " + self.gender)

u1 = User("Febin", 24, "Male")
u1.displayDetails()

#Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Your current balance is:- Rs", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount <= self.balance:
            self.balance = self.balance - self.amount
            print("Rs {} withdrawn\n".format(self.amount))
            print("Your current balance is Rs {}".format(self.balance))
        else:
            print("Insufficient funds")

    def viewBalance(self):
        self.displayDetails()
        print("Balance:- ", self.balance)

b1 = Bank("Raghu", 24, "Male")
# print(b1.name)
# print(b1.age)
b1.deposit(30)
b1.deposit(80)
b1.viewBalance()
b1.withdraw(110)
b1.viewBalance()
