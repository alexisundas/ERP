""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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
                      "Show the oldest person",
                      "Closest person to the average year",
                      "Back to main menu"]
                    
    ui.print_menu("Store Menu", menu_for_store, "Exit program")
    
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("hr/persons.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("hr/persons.csv"))
    elif option == "3":
        id_ = ui.get_inputs(["Enter the ID to be Removed:  "], "")
        remove(data_manager.get_table_from_file("hr/persons.csv"), id_)
    elif option == "4":
        id_ = ui.get_inputs(["Enter the ID to be Updated:  "], "")
        update(data_manager.get_table_from_file("hr/persons.csv"), id_)
    elif option == "5":
        result = get_oldest_person(data_manager.get_table_from_file("hr/persons.csv"))
        label = "The Oldest Person(s) is/are: " + "\n"
        ui.print_result(result,label)
        ui.get_inputs(["(0) Main Menu: "],"")
    elif option == "6":
        result = get_persons_closest_to_average(data_manager.get_table_from_file("hr/persons.csv"))
        label = "Person(s) Closest To Average: " + "\n"
        ui.print_result(result, label)
        ui.get_inputs(["(0) Main Menu: "],"")



def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "Name", "Year of Birth"]

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
    new_list_to_add.extend(ui.get_inputs(["Please add the Year of Birth: "],""))

    
    table.append(new_list_to_add) # hozzáadni a csv filehoz
    data_manager.write_table_to_file("hr/persons.csv", table)

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

    common.toremoveid("hr/persons.csv",data_manager.get_table_from_file("hr/persons.csv"),id_)


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
            i[1] = ui.get_inputs(["What should i update the name to: "],"")
            i[2] = ui.get_inputs(["What should I update the year of birth? "],"")
    data_manager.write_table_to_file("hr/persons.csv", table)

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    years = []
    for row in table:
        years.append(row[2])

    oldestpers = []
    for row in table:
        if row[2] == min(years):
            oldestpers.append(row[1])
    
     #### SHOWING ONLY ONE PERSON ! 
    
    return oldestpers


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    allyears = []

    for row in table:
        allyears.append(int(row[2]))

    avg_year = sum(allyears) / len((allyears))

    low = []
    high = []
    for year in allyears:
        if year < avg_year:
            low.append(year)
        if year > avg_year:
            high.append(year)

    nearestlow = max(low)
    nearesthigh = min(high)

    low_end = avg_year - float(nearestlow)
    high_end = float(nearesthigh) - avg_year

    thename = []
    for name in table:
        if low_end < high_end:
            if nearestlow == int(name[2]):
                thename.append(name[1])
        elif high_end < low_end:
            if nearesthigh == int(name[2]):
                thename.append(name[1])
    
    
    return thename
