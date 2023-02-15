n1=int(input("Enter the length of square:\n"))
areasquare=lambda x:x*x
print("Area",areasquare(n1))


n2=int(input("Enter the length of rectangle:\n"))
n3=int(input("Enter the breadth of rectangle:\n"))
arearect=lambda a,b:a*b
print("Area=",arearect(n2,n3))


n4=int(input("Enter the base of triangle:\n"))
n5=int(input("Enter the height of triangle:\n"))

areatri=lambda x,y:.5*x*y
print("Area=",areatri(n4,n5))
