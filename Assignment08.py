# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Beise, 12/6/2021, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
file_name = 'products.txt'
lstOfProductObjects = []
name = ""
Product = ""


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
        static: get_product_info()
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Beise, 12/6/2021,Modified code to complete assignment 8
    """


    # TODO: Add Code to the Product class
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Beise, 12/6/2021,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_products_objects):
        """ Write data to a file from a list of object rows
        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        message = False
        try:
            file = open(file_name, "w")
            for row in list_of_products_objects:
                file.write(row.__str__() + "\n")
            file.close()
            message = True
        except Exception as e:
            print("Error. Try again.")
            print(e, e.__doc__, type(e), sep='\n')
        return message

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of object rows
        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                row = line.split(",")
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print("Error. Try again.")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    @staticmethod
    def Product(self, first_name, last_name):
        print(first_name, last_name)


    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_options():
        print('''
        Menu of Options
        1) Show current names in list
        2) Add new names to list
        3) Save list of names to file and exit program
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_options():
        try:
            choice = input("Select an option [1 - 3]:  ").strip()
            if len(choice) == 0:
                raise Exception("Choice cannot be blank.")
        except ValueError as e:
            print("Choice cannot contain letters or characters.")
            print(e)
        print()
        return choice


    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_options(list_of_rows):
        print("The current names on your list are: ")
        for row in list_of_rows:
            print(row)
        print()

    # TODO: Add code to get product data from user
    @staticmethod
    def input_name_data(file_data):
        try:
            first_name = input("Enter first name: ").strip()
            if len(choice) == 0:
                raise Exception("Name cannot be blank.")
            elif choice.isdigit():
                raise Exception("Name cannot contain numbers.")
            last_name = input("Enter last name: ").strip()
            if len(choice) == 0:
                raise Exception("Name cannot be blank.")
            elif choice.isdigit():
                raise Exception("Name cannot contain numbers.")
            f = IO.Product(first_name, last_name)
            file_data.append(emp)
        except Exception as e:
            print(e)
        return file_data

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
file_data = []
file_data = FileProcessor.read_data_from_file(file_name)

while True:

    # Show user a menu of options
    IO.print_menu_options()

    # Get user's menu option choice
    choice = IO.input_menu_options()

    # Show user current data in the list of product objects
    if choice.strip() == '1':
        IO.print_current_options(file_data)

    # Let user add data to the list of product objects
    if choice.strip() == '2':
        IO.input_name_data(file_data)

    # let user save current data to file and exit program
    if choice.strip() == '3':
        FileProcessor.save_data_to_file(file_name, file_data)
        print("Goodbye!")
        break

# Main Body of Script  ---------------------------------------------------- #

