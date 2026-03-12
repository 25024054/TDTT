a=int(input("Nhập vào năm :"))
if a%400==0 or a%4==0 and a%100!=0:
 print(f"{a} là năm nhuận")
else:
 print(f"{a} không là năm nhuận")
