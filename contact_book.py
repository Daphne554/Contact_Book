name = input("Enter your name: ")
print(name + "'s Contact Book")

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
    option = input("Would you like to add, view or exit contact book (add/view/exit): ")
    if option == "exit":
        continue

    if option == "add":
        add()

    elif option == "view":
        view()

    else:
        print("Invalid option! Enter add/view/exit: ")
        break
