


principal =0
rate=0
time = 0



while principal <= 0 :
     principal = float(input(" enter principal amount : " ))
     if principal < 0 :
         print(f"it's smaller  {principal} ")

while rate <=0:
    rate = float(input("enter rate : "))
    if rate < 0 :
        print(f"its smaller{rate}")
while time <= 0:
    time = float(input("enter time : "))
    if time < 0 :
        print(f"its small{time}")
total = principal*pow((1+rate/100),time)
print(f"your balance is {total}")


