import calculator as c

print("***********************************")
print("Calculator in Action")
print("***********************************")

a = int(input("Enter first number: "))
b = int(input("Enter 2nd number: "))


print(c.add(a, b))
print(c.sub(a, b))
print(c.mul(a, b))
print(c.div(a, b))

print("And the Random number generated is: ", c.a)
