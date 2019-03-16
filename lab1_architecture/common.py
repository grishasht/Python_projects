import os as os
import pymongo as pm


client = pm.MongoClient("mongodb://localhost:27017/")
my_db = client["catalogue_data"]
my_col = my_db["collection"]


def print_catalogue(tmp_catalogue):
    print("\t{0:20s} {1:40s}". format(tmp_catalogue['Name'], tmp_catalogue['Phone_number']))


def get_dict(_dict, count):
    return dict(_dict[count])


def del_catalogue_elem(tmp, tmp_catalogue):
    return True if tmp_catalogue['Name'] == tmp else False


def show_catalogue(document, catalogue):
    print(" Catalogue:")
    i = 0
    while i < len(document):
        catalogue = get_dict(document, i)
        del catalogue['_id']
        print_catalogue(catalogue)
        i += 1


def print_cond(document, catalogue):
    if not list(document):
        print(" Catalogue is empty!")
    else:
        show_catalogue(document, catalogue)
    print()


def choise1(catalogue):
    catalogue = {'Name': input(" Write name and surname: "),
                 'Phone_number': input(" Write phone number: ")}
    my_col.insert_one(catalogue)
    input()


def choise2(document, catalogue):
    if not document:
        print(" Catalogue is empty, nothing to remove!")
    del_name = input(" Write name of person who you want to remove: ")
    for catalogue in document:
        if del_catalogue_elem(del_name, catalogue):
            my_col.delete_one(catalogue)
    input()


def prog_exit():
    print(" Exit\n")
    input()
    os.system('clear')


def switch(document, catalogue, var):
    var = int(input(" Your choise: "))
    if var == 1:
        choise1(catalogue)
    if var == 2:
        choise2(document, catalogue)
    if var == 0:
        prog_exit()
        return 0
