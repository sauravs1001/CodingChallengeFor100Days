dict = {}

while True:
    print("--------------------Birthday App-----------------------")
    print("1. Show Birthday")
    print("2. Add to Birthday List")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if len(dict.keys()) == 0:
            print("Nothing to show")
        else:
            name = input("Enter a name to look for birthday")
            birthday = dict.get(name, "No data found")
            print(birthday)
    elif choice == 2:
        name = input("Enter your Friend's Name")
        date = input("Enter Birthday in DD-Month-YYYY format")
        dict[name] = date
        print("Birthday Added")
    elif choice == 3:
        break
    else:
        print("Please choose a valid option")

