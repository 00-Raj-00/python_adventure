"""
num1 = 4
num2 = 5

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 // num2)
print(num1 ** num2)
_____________
num = - 34
num1 = 23
print(abs(num) , abs(num1))
----------------------------
# user input program

num = int(input("enter your number : "))
num1 = int(input("enter your number : "))
print(f"addition of this number {num+num1} ")
print(f"difference of this {num-num1}")
print(f"product of this : {num*num1}")
-------------------------------------
num = int(input("enter your value "))
if num >0:
    print("positive")
elif num < 0 :
    print("negative")
else :
    print("zero")
----------------

num = int(input("enter your value : "))
if num % 2==0:
    print("even")
if num % 2 != 0 :
    print("odd")
"""
num = int(input("enter you value : "))
num1 = int(input("enter your value :"))
if num > num1 :
    print(f"{num}is greater that {num1}")
elif num == num1  :
    print(f"{num} is equal to {num1}")
else:
    print(f"{num1} is greater than {num}")