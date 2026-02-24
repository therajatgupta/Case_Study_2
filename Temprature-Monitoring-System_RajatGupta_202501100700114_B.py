# -----------------------------------------------------------
# Grocery Billing System
# Name: Rajat Gupta
# Roll No: 202501100700114
# Branch: ECE-B
# -----------------------------------------------------------

#importing the uniform func from random module
from random import uniform as temp
import time 

#Asking max and min limit of temprature from user
min_temp,max_temp = map(int,input("Enter the min and max limits of temprature respectively: ").split())
time.sleep(0.5)

print("-------------------------------")

while True:
    print("Acquiring the temprature value...")
    time.sleep(1)
    temprature = round(temp(0,100),2)
    print("Temprature Acquried...:",temprature)
    time.sleep(1)

    if temprature>max_temp:
        for char in "Alert: Temperature is too high":
            print(char,flush=False,end="")
            time.sleep(0.05)
        print("\n-------------------------------")
    elif temprature>min_temp:
        for char in "Temperature is within acceptable limit":
            print(char,flush=False,end="")
            time.sleep(0.05)
        print("\n-------------------------------")
    else:
        for char in "Alert: Temperature is too low":
            print(char,flush=False,end="")
            time.sleep(0.0520 )
        print("\n-------------------------------")
    
    time.sleep(2)
    


