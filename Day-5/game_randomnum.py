import random

a = random.randint(0, 20)

while True:
    b = int(input("Enter a number"))
    if b==a:
        print("Game Over !!!")
        break
    elif b>a:
        print("Enter a smaller number")
    elif b<a:
        print("Enter a bigger number")

print("***************************")
print("The random number is", a)

