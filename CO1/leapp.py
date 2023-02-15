start_year=int(input("Enter the start year"))
end_year=int(input("Enter the last year"))
print("The first year is", start_year,"the last year is",end_year)
print("List of leap year:")
for i in range(start_year,end_year):
    if(i%4==0)and(i%100!=0)or((i%400==0)and(i%100==0)):
        print(i,"is a leap year")
