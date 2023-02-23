from Contact import Contact
#i think this is how you make variables in python
program = True
global name
global address
global contact
contact = Contact("", "", "")

print("Welcome to the Contact Book")
while(program):
    #storing all current names, addresses, and phone numbers


    print("1. Enter Contact\n2.Add Contact\n3.Exit")
    get_input = int(input("Choose option: "))
    
    if(get_input == 1):
        name = input("Enter name: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        contact = Contact(name, address, phone)
    elif(get_input == 2):
        if (contact.name == ""):
            print("Enter a contact first.")
        else:
            contact.add_contact()
    elif(get_input == 3):
        print("Goodbye")
        program = False
    else:
        print("Invalid option")