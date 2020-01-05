""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""


# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
   # YOUR CODE
    menu_for_store = ["Show Table",
                      "Add",
                      "Remove",
                      "Update",
                      "Count by Manufacturer",
                      "Average Games in stock by Manufacturer",
                      "Back to main menu"]
                    
    ui.print_menu("Store Menu", menu_for_store, "Exit program")
    
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("store/games.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("store/games.csv"))
    elif option == "3":
        id_ = ui.get_inputs(["Enter the ID to be Removed:  "], "")
        remove(data_manager.get_table_from_file("store/games.csv"), id_)
    elif option == "4":
        id_ = ui.get_inputs(["Enter the ID to be Updated:  "], "")
        update(data_manager.get_table_from_file("store/games.csv"), id_)
    elif option == "5":
        result = get_counts_by_manufacturers(data_manager.get_table_from_file("store/games.csv"))
        label = ""
        ui.print_result(result, label)
        ui.get_inputs(["(0)Main Menu "], "")
    elif option == "6":
        manufacturer = ui.get_inputs(["Enter a manufacturer: "], "")
        label = manufacturer[0]
        result = get_average_by_manufacturer(data_manager.get_table_from_file("store/games.csv"), label)
        ui.print_result(result,label)
        ui.get_inputs(["(0)Main Menu :"], "")


def show_table(table):

    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    
    title_list = ["ID", "Title", "Manufacturer", "Price", "IN STOCK"]

    ui.print_table(table, title_list)

    inputs = ui.get_inputs(["Please enter a number: "], "")
    if inputs == 0:
        pass

    





def add(table):

    """     first_question = "Please add the Title: "
    second_question = "Please add the Manufacturer: "
    third_question = "Please add the Price: "
    fourth_question = "Please add the Stock: " """


    new_list_to_add = []

    new_list_to_add.append(common.generate_random(table))
    new_list_to_add.extend(ui.get_inputs(["Please add the Title: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the Manufacturer: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the Price: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the Stock: "],""))

    table.append(new_list_to_add) # hozzáadni a csv filehoz
    data_manager.write_table_to_file("store/games.csv", table)
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    return table

def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    common.toremoveid("store/games.csv",data_manager.get_table_from_file("store/games.csv"),id_)




def update(table, id_):

    for i in table:
        if i[0] == id_:
            i[1] = ui.get_inputs(["What should i update the title to: "],"")
            i[2] = ui.get_inputs(["What should i update the manufacturer to? "],"")
            i[3] = ui.get_inputs(["What should i update the price to? "],"")
            i[4] = ui.get_inputs(["What sould i update the stock number? "],"")
    data_manager.write_table_to_file("store/games.csv", table)
            
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):

    how_many_games = {}

    for elements in table:
        if elements[2] not in how_many_games.keys():
            how_many_games[elements[2]] = 1
        else:
            how_many_games[elements[2]] += 1


    return how_many_games


    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    count = []
    try:
        for elements in table:
            if elements[2] == manufacturer:
                count.append(elements[4])
            
        x = 0
        for number in count:
            x += int(number)

        lastresult = x / len(count)

        
        return lastresult
    except ZeroDivisionError :
        ui.print_error_message("There is no such a Manufacturer")
