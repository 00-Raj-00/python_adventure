import time
import random


print(" let's start game rock , paper , scissor ")
time.sleep(1)

for x in range(1,4):
    a = random.randint(1, 3)
    print(a)
    if a == 1:
        print("Scissor")


        time.sleep(3)

    elif a == 2 :
        print("Paper")
        time.sleep(3)

    elif a == 3 :
        print("Rock")
        time.sleep(3)
