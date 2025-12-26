year=int(input(" enter the year: "))
if(year%400==0) or (year%4==0 & year%100!=0):
    print(" the year is leap")
else:
    print(" the year is not leap year")    
