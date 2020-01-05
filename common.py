""" Common module
implement commonly used functions here
"""

import random
import string
import data_manager

def generate_random(table):
    
    id_number = random.choice(string.ascii_lowercase)
    id_number += random.choice(string.ascii_uppercase)
    id_number += random.choice(string.digits)
    id_number += random.choice(string.digits)
    id_number += random.choice(string.ascii_uppercase)
    id_number += random.choice(string.ascii_lowercase)
    id_number += random.choice(string.punctuation)
    id_number += random.choice(string.punctuation)

    li = list(id_number)

    for i in li:
        if i == ";":
            asd = li.index(";")
            li[asd] = "."
        else:
            pass

    join_list = ''

    join_list.join(li)
    

    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    # your code

    return join_list.join(li)

def convert(list):
    
    # Converting integer list to string list 
    s = [str(i) for i in list]
    
    # Join list items using join() 
    res = int("".join(s)) 
    return(res)


def toremoveid(path,table,id_):

    for row in table:
        if id_[0] in row:
            table.remove(row)
    
    data_manager.write_table_to_file(path, table)

    return table




""" 
def add(table):
    new_list_to_add = []

    new_list_to_add.append(common.generate_random(table))
    new_list_to_add.append(ui.get_inputs([first_question],""))
    new_list_to_add.append(ui.get_inputs([second_question],""))
    new_list_to_add.append(ui.get_inputs([third_question],""))
    new_list_to_add.append(ui.get_inputs([fourth_question],""))
    
    table.append(new_list_to_add) # hozzáadni a csv filehoz
    data_manager.write_table_to_file("store/games.csv", table)

    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    

    # your code

    return table """

def linespace(list):      
    i = 0
    for num in list:
        i += num

    print("|" + ("-" * i) + (len(list) - 2) * "-" + "|")