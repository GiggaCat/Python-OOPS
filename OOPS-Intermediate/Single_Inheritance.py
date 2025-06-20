#Single Inheritance occur when child class inherits only a single parent class...

#Base class
class company:                                            
    def __init__(self,name,company,language,emp_ID,age):
        self.name=name
        self.company=company
        self.language=language
        self.emp_ID=emp_ID
        self.age=age

#Child class or Derived class
#Class Programmer is derived from class company   
class Programmer(company):
    def emp_status(self):
        print(f"Programmer name: {self.name}\nProgrammer Company: {self.company}\nProgrammer language: {self.language}\nProgrammer Emp_ID: {self.emp_ID}\nProgrammer Age: {self.age}\n")

emp1 = Programmer("Vansh","Microsoft","Python","001",19)
emp1.emp_status()

emp2 = Programmer("Arun","Infosys","Javascript","002",21)
emp2.emp_status()