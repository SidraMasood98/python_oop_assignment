class Employee:
    pass
    def __init__(self, name, salary, ssn):
        pass
        self.name = name
        self._salary = salary
        self.__ssn = ssn

if __name__ == "__main__":
    pass
    emp = Employee("sidra", 100000, 1234-56789)

    # access public variable:
    print("public variable:", emp.name)

     # access protected variable:
    print("protected variable:", emp._salary)

     # access public variable:
    try:
        print("public variable:", emp.__ssn)

    except AttributeError:
        print("cannot access private variable __ssn")
        