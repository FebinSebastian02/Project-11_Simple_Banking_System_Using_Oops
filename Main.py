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
b1 = Bank("Raghu", 24, "Male")
print(b1.name)
print(b1.age)
