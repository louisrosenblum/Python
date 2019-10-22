# -----------------------------------------------------
# CSCI 127, Lab 8
# October 24, 2017
# Anthony Rosenblum
# -----------------------------------------------------

class Contact:

    def __init__(self,first_name,last_name,cell_number):
        self.first_name = first_name
        self.last_name = last_name
        self.cell_number = cell_number

##    def get_first_name(self):
##        return str(self.first_name)
##
##    def get_last_name(self):
##        return str(self.last_name)

    def get_cell_number(self):
        return str(self.cell_number)

    def get_area_code(self):
        return str(self.cell_number)[:3]

    def __str__(self):
        x = str(self.first_name) + " " + str(self.last_name) + " " 
        y = x.ljust(25) + str(self.cell_number)
        return y

    def set_first_name(self,first_name):
        self.first_name = first_name

    def set_title(self,title):
        self.first_name = str(title) + " " + str(self.first_name)

# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("My Contacts")
    print("-----------")
    for person in contacts:
        print(person)
    print("-----------\n")

# -----------------------------------------------------

def main():
    champ = Contact("???", "Bobcat", "406-994-0000")
    president = Contact("Waded", "Cruzado", "406-994-CATS")
    professor = Contact("John", "Paxton", "406-994-4780")

    contacts = [champ, president, professor]

    print_directory(contacts)

    champ.set_first_name("Champ")
    president.set_title("President")
    professor.set_title("Professor")

    print_directory(contacts)

    print("The area code for cell number", champ.get_cell_number(), "is", \
           champ.get_area_code())

# -----------------------------------------------------

main()
