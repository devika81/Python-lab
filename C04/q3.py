class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area1(self):
        self.a1=self.length*self.width
        print("Area=",self.a1)
    def __lt__(self,a2):
        if self.a1<a2.a1:
            return True
        else:
            return False
l1=int(input("Enter the length of first rectangle:"))
w1=int(input("Enter the width of first rectangle:"))
l2=int(input("Enter the length of second rectangle:"))
w2=int(input("Enter the width of second rectangle:"))
obj1=Rectangle(l1,w1)
obj2=Rectangle(l2,w2)
obj1.area1()
obj2.area1()
if obj1<obj2:
    print("Second rectangle is large")
else:
    print("First rectangle is large or are equal")
