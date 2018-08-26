def hello():
    return 1,2,3,4

a =[]

for i in hello():
    a.append(i)

print(a)

# To return multiple values in a function we can use a list or a tuple