print("")

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

while True:
    option = input("Would you like to add contacts, delete contacts, edit contacts or exit contact book (add/view/delete/edit/exit): ")
    if option == "exit":
        continue

    if option == "add":
        add()

    elif option == "view":
        view()

    elif option == "edit":
        pass

    elif option == "delete":
        pass
    else:
        print("Invalid option! Enter add/view/delete/edit/exit: ")
        break
