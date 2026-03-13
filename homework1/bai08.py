a=input("Nhập tên chủ hộ :")
b=int(input(" Nhập số điệnt tháng trước :"))
c=int(input(" Nhập số điệnt tháng này :"))
if 0<=c-b<=50:
 print(f"Ho va ten:{a}\nTien phai tra la :{int(1.08*(c-b)*1984)}")
elif 51<=c-b<=100:
 print(f"Ho va ten:{a}\nTien phai tra la :{int(1.08*((c-b-50)*2050+50*1984))}")
elif 101<=c-b<=200:
 print(f"Ho va ten:{a}\nTien phai tra la :{int(1.08*((c-b-100)*2380+50*1984+50*2050))}")
elif 201<=c-b<=300:
 print(f"Ho va ten:{a}\nTien phai tra la :{int(1.08*((c-b-200)*2998+100*2380+50*1984+50*2050))}")
elif 301<=c-b<=400 :
 print(f"Ho va ten:{a}\nTien phai tra la :{int(1.08*((c-b-300)*3350+100*2998+100*2380+50*1984+50*2050))}")
elif c-b>=401:
 print(f"Ho va ten:{a}\nTien phai tra la :{int(1.08*((c-b-400)*3460+100*3350+100*2998+100*2380+50*1984+50*2050))}")
       
