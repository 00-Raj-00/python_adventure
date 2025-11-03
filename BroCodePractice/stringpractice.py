
#validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

name = input("Enter your name : ")
length_of_name = len(name )
space_present = name.count(" ")
digit_present = name.isalpha()
if length_of_name >=12 :
    print("Invalid name must be in 12 character")
if space_present >=1:
    print("please remove space from your name ")
if  digit_present == False:
    print("please remove digit from your name ")
print(name,length_of_name,space_present,digit_present)
