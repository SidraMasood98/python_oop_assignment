class Dog:
    def __init__(self, name, breed):
        self.name = name # instance variable
        self.breed = breed  # instance variable

    def bark (self): # instance method
        print(f"{self.name} is barking!")

if __name__ == "__main__":
 my_dog = Dog ("tommy", "Labrador") # creating object instance
 my_dog.bark() # call the method
        