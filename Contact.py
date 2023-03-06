class Contact:
    #all Contact objects will open the same Contacts file. this is intentional
    #ideally, only one Contact object will be instantiate
    global filename
    filename = "Contacts.txt"

    def __init__(self, name, address, phoneNo):
        self.name = name
        self.address = address
        self.phoneNo = phoneNo

    def change_name(self, inputName):
        self.name = inputName
        
    def change_address(self, input_address):
        self.address = input_address

    def change_phoneNo(self, input_phoneNo):
        self.phoneNo = input_phoneNo

    def add_contact(self):
        with open(filename, "a") as file:
            file.write("{\n NAME:" + self.name + "\n ADDRESS:" + self.address + "\n PHONE:" + self.phoneNo + "\n" + "}\n")

    def delete_contact(self):
        print("foobar")

    #getters
    #these all return an array of name, address, and phoneNo for the driver
    #if its empty uhhh idk lol

    def get_names(self):
        names = []
        with open(filename, 'r') as file:
            line = file.readline()
            while line:
                print(line)
                line = file.readline()
                if "NAME:" in line:
                    print("NAME FOUND")
                    names.append(line[6:int((len(line)-1))])
        if not names:
            print("No names detected!")
        else:
            return names


    


    

