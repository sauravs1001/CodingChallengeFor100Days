import keyword

for key in keyword.kwlist:
    print(key)

print("=========================================================")
print("Total number of keywords is:" + str(len(keyword.kwlist)))
