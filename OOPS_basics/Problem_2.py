#Create a class programmer for storing the information of few programmer working at Microsoft

class programmer:
    company = "Microsoft"
    def __init__(self,name,language,city,age):
        self.name=name
        self.language=language
        self.city=city
        self.age=age
    def get_info(self):
        print(f"Programmer name: {self.name}\nProgrammer language: {self.language}\nProgrammer city: {self.city}\nProgrammer age: {self.age}\n")


p1 = programmer("Vansh","python","delhi",20)
p1.get_info()

p2 = programmer("Ansh","Javascript","pune","24")
p2.get_info()
