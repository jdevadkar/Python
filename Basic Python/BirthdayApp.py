# created Empty dictinary.
dict = {}
# While Loop
while True:
    print("---------- Birthday App -----------")
    print("1.Show Birthday")
    print("2. Add birthday to List")
    print("3.Show All List")
    print("4.Exit")
    #Getting User Choice
    choice = int(input("Enter the Choice : "))
    #Showed Friends Birthday
    if choice == 1:
        if len(dict.keys()) == 0:
            print("Nothing to Show ")
        else:
            name =  input("Enter Name to look for Birthday : ")
            birthday =dict.get(name, "No data Found")
            print(birthday)
    # Added Birthday in Dictinary
    elif choice == 2:
        name = input("Enter Friends Name: ")
        birthday = input("Enter Friends Birthdate : ")
        dict[name] = birthday
        print("Birthday Added")
    # Showed All birthday In Dictionary
    elif choice == 3:
        for key in dict:
            print(key ,'->',dict[key])
    # Exit
    elif choice == 4:
        break
    else:
        print("Choose a valid Option")