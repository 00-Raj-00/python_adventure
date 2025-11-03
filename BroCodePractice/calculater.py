

val1 = float(input("please enter first value : "))
choice = input("please enter choose operator: + ,- ,/ ,*  : ")
val2 = float(input("please enter second value : "))

if choice=="+":
    result = val1+val2
    print(f"result = {result}" )
elif choice =="-" :
    result = val1 - val2
    print(f"result = {result}")
elif choice =="/" :
    result = val1 / val2
    remainder = val1 % val2
    print(f"result = {result}   reminder = {remainder}")
elif choice == "*":
     result = val1 * val2
     print(f"result = {result}")
else :
    print("this is wrong input ")



