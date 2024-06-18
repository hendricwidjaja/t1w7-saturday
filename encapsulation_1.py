class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.__age = age # Private attribute
        self.__email = email # Private attribute
    
    # Getter for age
    def get_age(self):
        return self.__age
    
    # Setter for age
    def set_age(self, age):
        self.__age = age

    # Getter for email
    def get_email(self):
        return self.__email
    
    # Setter for email
    def set_email(self, email):
        self.__email = email
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.__age}, Email: {self.__email}"
    
# Create an object
person1 = Person("John Doe", 30, "john.doe@example.com")

# Accessing and modifying age using getter and setter
print(person1.get_age())
person1.set_age(31)
print(person1.get_age())

print(person1.get_email())
person1.set_email("john.new@example.com")
print(person1.get_email())

print(person1.display_info())
