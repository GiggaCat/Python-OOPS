#Create a class train which has method to book a train, find train number, search for status and train fare

from random import randint
class train:
    def __init__(self,trainno,fro,to):
        self.trainno=trainno
        self.fro=fro
        self.to=to
    def book(self):
        print(f"Your train ticket from {self.fro} to {self.to} has been confirmed!!!")
    
    def train_no(self):
        print(f"The train number from {self.fro} to {self.to} alloted to you is {self.trainno}")

    def status(self):
        print(f"Your train {self.trainno} is running on time!!!")

    def train_fare(self):
        fare = randint(222,1001)
        print(f"The fair for train number {self.trainno} from {self.fro} to {self.to} is ₹{fare}")

t1 = train("1231","Delhi","Jaipur")
t1.book()
t1.train_no()
t1.status()
t1.train_fare()