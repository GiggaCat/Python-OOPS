#Multiple Inheritance occurs when the child class inherits from more than one parent class....

#Base class or Parent class 1
class company:
        company_name="Microsoft"
        company_location="Delhi"

#Base class or Parent class 2
class status:
    company_status="Hiring"

#Base class or Parent class 3
class employee:
    def __init__(self,name,emp_ID,age):
        self.name=name
        self.emp_ID=emp_ID
        self.age=age

#Child class or Derived class
#Class programmer is derived from Classes(company,status,employee)
class programmer(company,status,employee):
    def stats(self):
        print(f"Company name: {self.company_name}\nCompany Location: {self.company_location}\nCompany Status: {self.company_status}\n")
    def emp_stats(self):
        print(f"Employee name: {self.name}\nEmployee Emp_ID: {self.emp_ID}\nEmployee Age: {self.age}\n")

emp1 = programmer("Vansh","001",19)
emp1.stats()
emp1.emp_stats()
        
    
emp2 = programmer("Ansh","002",20)
emp2.emp_stats()