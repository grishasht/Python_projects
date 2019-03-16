import common as com


def menu():
    choise = 1
    while choise != 0:
        com.os.system('clear')
        print(" Choose action\n 1 -- add new person into catalogue")
        print(" 2 -- delete person from catalogue\n 0 -- exit\n")
        document = list(com.my_col.find())
        catalogue = {}
        com.print_cond(document, catalogue)
        choise = com.switch(document, catalogue, choise)
