class Time:
    sum=0
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def sum(self):
        self.sum = self.hour*60*60+self.minute*60+self.second
    def __add__(self,second):
        return self.sum + second.sum
hour1 = int(input("Enter hour:"))
minute1 = int(input("Enter minute:"))
second1 = int(input("Enter second:"))
print("Time 1 is = ",hour1,":",minute1,":",second1,"AM","\n");
hour2 = int(input("Enter hour:"))
minute2 = int(input("Enter minute:"))
second2 = int(input("Enter second:"))
print("Time 2 is = ",hour2,":",minute2,":",second2,"PM","\n")
ob1 = Time(hour1,minute1,second1)
ob2 = Time(hour2,minute2,second2)
ob1.sum()
ob2.sum()
s=ob1+ob2
hour = int(s/3600)
min = int((s%3600)/60)
sec = int((s% 3600)%60)
print("The sum of two times = {0} hours: {1} mins: {2} secs".format(hour,min,sec))
