a=int(input("Nhập vào 1 số nguyên :"))
n=[0,5]
if a%3==0 and int(str(a)[-1])in n:
 print(f"{a} là số chia hết cho 3")
else :
 print(f"{a} là 1 số không chia hết cho 3 ")