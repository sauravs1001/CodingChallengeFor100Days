import random

heros = ["Shahrukh Khan", "Salman Khan", "Hrithik Roshan", "Amir Khan", "Ranveer Singh"]


a = random.randint(0, len(heros))

name = input("Enter your name: ")

print(name + " looks like " + heros[a])