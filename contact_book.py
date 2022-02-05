print("THE CONTACT BOOK")
def add():
    name = input("Name: ")
    number = input("Mobile: ")
    number2 = input("Phone: ")
    email = input("Email: ")

    with open("contactbook.txt", 'a') as c:
        c.write("Name: " + name + " | Mobile: " + number + " | Phone: " + number2 + " | Email: " + email + "\n")


def view():
    with open("contactbook.txt",'r') as c:
        for line in c.readlines():
            print(line.rstrip())


def delete():
    del_info = input("Enter contact name to delete all contact information: ").lower()
    with open("contactbook.txt",'r') as c:
        file = c.readlines()
    with open("contactbook.txt",'r') as c:
        for line in file:
            words = line.strip("\n").lower().split(' ')
            if del_info.lower() not in words:
                print(line)


def search():
    search_name = input("Enter contact name to search: ").lower()
    with open("contactbook.txt", 'r') as c:
        file = c.readlines()
    with open("contactbook.txt", 'r') as c:
        for line in file:
            words = line.strip("\n").lower()
            if search_name.lower() in words:
                print(line)
            else:
                print("Contact not found! ")

while True:
    option = int(input(" 1.Add new contact\n 2.View contact list\n 3.Search contact\n 4.Delete "
                       "contact\n 5.Exit contact book\n 0.To begin to return to options\n Enter option number: "))
    if option == 5:
        quit()

    if option == 0:
        continue

    if option == 1:
        add()

    elif option == 2:
        view()

    elif option == 3:
        search()

    elif option == 4:
        delete()

    else:
        print("Invalid number ! Type number assigned option! ")
        break
