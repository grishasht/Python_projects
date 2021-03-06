import os as os
import pymongo as pm


client = pm.MongoClient("mongodb://localhost:27017/")
my_db = client["catalogue_data"]
my_col = my_db["collection"]


def print_catalogue(tmp_catalogue):
    # Prints phone catalogue on users console
    print("\t{0:20s} {1:40s}". format(tmp_catalogue['Name'],
                                      tmp_catalogue['Phone_number']))


def get_dict(_dict, count):
    # Remake MongoDB document to dict
    """
    >>> get_dict([{'Name': "Grisha"}, {'Phone': "0501234567"}], 1)
    {'Phone': '0501234567'}
    >>> get_dict([{'Name': "Grisha"}, {'Phone': "0501234567"}], 0)
    {'Name': 'Grisha'}
    >>> get_dict([{'Name': "Grisha"}, {'Phone': "0501234567"}, {'Name': 'Hennadiy'}], 2)
    {'Name': 'Hennadiy'}
    """
    return dict(_dict[count])


def del_catalogue_elem(tmp, tmp_catalogue):
    # Removes phone catalogue item
    """
    >>> del_catalogue_elem("Grisha", {"Name": "Grisha"})
    True
    >>> del_catalogue_elem("Heorhii", {'Name': "Andrew"})
    False
    """
    return True if tmp_catalogue['Name'] == tmp else False


def show_catalogue(document):
    # Prints catalogue from MongoDB document
    print(" Catalogue:")
    i = 0
    while i < len(document):
        catalogue = get_dict(document, i)
        del catalogue['_id']
        print_catalogue(catalogue)
        i += 1


def print_cond(document, catalogue):
    # Prints phone catalogue if its not empty
    if not list(document):
        print(" Catalogue is empty!")
    else:
        show_catalogue(document)
    print()


def choice1(catalogue):
    # Input new item to phone catalogue
    catalogue = {'Name': input(" Write name and surname: "),
                 'Phone_number': input(" Write phone number: ")}
    my_col.insert_one(catalogue)
    input()


def choice2(document, catalogue):
    # Removes item from phone catalogue
    if not document:
        print(" Catalogue is empty, nothing to remove!")
    del_name = input(" Write name of person who you want to remove: ")
    for catalogue in document:
        if del_catalogue_elem(del_name, catalogue):
            my_col.delete_one(catalogue)
    input()


def prog_exit():
    # Prints program exit and clears terminal
    print(" Exit\n")
    input()
    os.system('clear')


def switch(document, catalogue):
    # Condition function.
    # Depending on menu input implements program algorithms
    var = int(input(" Your choise: "))
    if var == 1:
        choice1(catalogue)
    if var == 2:
        choice2(document, catalogue)
    if var == 0:
        prog_exit()
        return 0
