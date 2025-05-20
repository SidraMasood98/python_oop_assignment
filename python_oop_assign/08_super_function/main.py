
# step 1 parent class:
class Person:
    def __init__(self, name):
        self.name = name

# step 2 child class:
class Teacher(Person): # inheriting person
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# step 3: display:
    def display(self):
        print(f"Name: {self.name}, subject: {self.subject}")

# creating object:
if __name__ == "__main__":
    teacher = Teacher("Miss Sidra", "Mathematics")
    teacher.display()