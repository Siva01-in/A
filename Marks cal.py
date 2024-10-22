'''it a internal mark calculator
it create a for lreaning purpose'''
import time
print("Welcome to Marks Calculation ")
a=int(input("Enter a actual marks:"))
t=int(input("Enter a total marks:"))

e=int(input("Enter a internal %ke 25 or 50 or 100:"))
c=(a/t)*100
print(time.sleep(2),"it time to calculation it will a percentage:\n",c,"%")
d=(c/100)*e
print("It a percent ",d,"it is round:",round(d))