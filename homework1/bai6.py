import math
a=float(input(" NHập vào 1 cạnh :"))
b=float(input(" NHập vào 1 cạnh :"))
c=float(input(" NHập vào 1 cạnh :"))
if a+b>c and a+c>b and b+c>a :
 p=(a+b+c)/2
 s= math.sqrt(p*(p-a)*(p-b)*(p-c))
 print(f"{s:.1f}")
else:
 print( "Khong phai 3 canh cua tam giac")
 
