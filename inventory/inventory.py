""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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

    
    menu_for_store = ["Show Table",
                      "Add",
                      "Remove",
                      "Update",
                      "Item by Durability Time",
                      "Average Durability Time by Manufacturer",
                      "Back to main menu"]
                    
    ui.print_menu("Store Menu", menu_for_store, "Exit program")
    
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("inventory/inventory.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("inventory/inventory.csv"))
    elif option == "3":
        id_ = ui.get_inputs(["Enter the ID to be Removed:  "], "")
        remove(data_manager.get_table_from_file("inventory/inventory.csv"), id_)
    elif option == "4":
        id_ = ui.get_inputs(["Enter the ID to be Updated:  "], "")
        update(data_manager.get_table_from_file("inventory/inventory.csv"), id_)
    elif option == "5":
        year = ui.get_inputs(["Enter the year of Durability: "], "Years of Durability")
        result = get_available_items(data_manager.get_table_from_file("inventory/inventory.csv"),year[0])
        ui.print_result(result,"Items not exceeding " + year[0] + " years of durability" + "\n")
        ui.get_inputs(["(0) Main Menu: "],"")
    elif option == "6":
        label = "Average Durability By Manufacturers: " + "\n"
        ui.print_result(get_average_durability_by_manufacturers(data_manager.get_table_from_file("inventory/inventory.csv")),label)
        ui.get_inputs(["(0) Main Menu: "],"")

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "Name", "Manufacturer", "Year of Purchase", "Durability"]

    ui.print_table(table, title_list)

    inputs = ui.get_inputs(["Please enter a number: "], "")
    if inputs == 0:
        pass


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    new_list_to_add = []

    new_list_to_add.append(common.generate_random(table))
    new_list_to_add.extend(ui.get_inputs(["Please add the Name: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the Manufacturer: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the Year of Purchase: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the Durability Time in Year/s: "],""))
    
    table.append(new_list_to_add) # hozzáadni a csv filehoz
    data_manager.write_table_to_file("inventory/inventory.csv", table)

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

    common.toremoveid("inventory/inventory.csv",data_manager.get_table_from_file("inventory/inventory.csv"),id_)


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    for i in table:
        if i[0] == id_:
            i[1] = ui.get_inputs(["What should i update the titel to: "],"")
            i[2] = ui.get_inputs(["What should I update the manufacturer to? "],"")
            i[3] = ui.get_inputs(["What should I update the year of purchase to? "],"")
            i[4] = ui.get_inputs(["What should I update the durability time in year/s? "],"")
    data_manager.write_table_to_file("inventory/inventory.csv", table)

    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """
    durability =[]
    for row in table:
        if row[4] < year[0]:
            durability.append(row)
    result = []
    index = 1
    for index , row in enumerate(durability):
        result.append(str(index) + "." + " , ".join(row) )
        index += 1
    
    

    return result




def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    sum_of_each_dur = {}

    for elements in table:
        if elements[2] not in sum_of_each_dur.keys():

            sum_of_each_dur[elements[2]] = [int(elements[4])]
            
        else:
            sum_of_each_dur[elements[2]] += [int(elements[4])]
    
    avg_list = {}
    
    for key in sum_of_each_dur:
        value = sum_of_each_dur[key]
        avg = sum(value) / len(value)
        avg_list[key] = avg



            


    return avg_list