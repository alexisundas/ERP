""" User Interface (UI) module """
import main
import os
import common

def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """




    longest_string = [0] * len(title_list)

    for row in table:
        for index in range(0, len(row)):
            if longest_string[index] < len(row[index]):
                longest_string[index] = len(row[index])
        
    for index, titles in enumerate(title_list):
        if longest_string[index] < len(title_list[index]):
            longest_string[index] = len(title_list[index])

    for index, titles in enumerate(title_list):
        print(((int(longest_string[index]) - len(titles)) * " ") + titles, end = "|")
        if index == len(title_list) - 1:
            print("")
            common.linespace(longest_string)


    for item in table:
        for index in range(len((title_list))):
            print(((int(longest_string[index]) - len(item[index])) * " ") + item[index] ,end= "|")
            if index == len(title_list) - 1:
                print("")
                common.linespace(longest_string)

    print("\n" + "(0)Main Menu")

def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    if isinstance(result,float):
        print(label , result)
    elif isinstance(result,dict):
        for k,v in result.items():
            print(k, v)
    elif isinstance(result,int):
        print(label ,result)
    elif isinstance(result,str):
        print(label , result)
    elif isinstance(result,list):
        result = "\n" + "\n".join(result)
        print(label , result )
    
    print("\n")

    
    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    os.system("clear")
    i = 0
    print(title + ": \n")

    for data in list_options:
        i += 1
        if i == 7:
            i = 0
        print(" " * 4 + "("+str(i)+")"+data)
    





def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    input_to_add_to_inputs = input(",".join(list_labels))
    inputs.append(str(input_to_add_to_inputs))
    os.system("clear")

    # your code

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("Error : " + message)