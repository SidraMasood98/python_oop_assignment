class Student:
    pass
    def __init__(self,name,marks):
        pass
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}, Score: {self.marks}")

if __name__ == "__main__":
    Student1= Student("sidra", 85)
    Student1.display()