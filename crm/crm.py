""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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
                      "ID of the Person Longest Name",
                      "Get Subscribed Emails and Names",
                      "Back to main menu"]
                    
    ui.print_menu("Store Menu", menu_for_store, "Exit program")
    
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("crm/customers.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("crm/customers.csv"))
    elif option == "3":
        id_ = ui.get_inputs(["Enter the ID to be Removed:  "], "")
        remove(data_manager.get_table_from_file("crm/customers.csv"), id_)
    elif option == "4":
        id_ = ui.get_inputs(["Enter the ID to be Updated:  "], "")
        update(data_manager.get_table_from_file("crm/customers.csv"), id_)
    elif option == "5":
        result = get_longest_name_id(data_manager.get_table_from_file("crm/customers.csv"))
        label = "Customer/s with the longest name and their ID:" + "\n"
        ui.print_result(result,label)
        ui.get_inputs(["(0) Main Menu : " + "\n"], "")
    elif option == "6":
        result = get_subscribed_emails(data_manager.get_table_from_file("crm/customers.csv"))
        label = "Subscribed People's Names and Emails: " + "\n"
        ui.print_result(result,label)
        ui.get_inputs(["(0) Main Menu : " + "\n"], "")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "Name", "E-mail", "Subscribed"]

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
    new_list_to_add.extend(ui.get_inputs(["Please add the e-mail: "],""))
    new_list_to_add.extend(ui.get_inputs(["Is She/He a Subscriber to the Newsletter? 1/0 = yes/no \n"],""))
    '''common.convert(ui.get_inputs)
    if ui.get_inputs == 1:
        ui.get_inputs = str
        new_list_to_add.append
    if ui.get_inputs == 0:
        ui.get_inputs = str
        new_list_to_add.append'''
    
    
    table.append(new_list_to_add) # hozzáadni a csv filehoz
    data_manager.write_table_to_file("crm/customers.csv", table)

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

    common.toremoveid("crm/customers.csv",data_manager.get_table_from_file("crm/customers.csv"),id_)



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
            i[2] = ui.get_inputs(["What should I update the e-mail to? "],"")
            i[3] = ui.get_inputs(["What should I update the subscribe status to? "],"")
    data_manager.write_table_to_file("crm/customers.csv", table)

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    name = []
    for row in table:
        name.append(len(row[1]))

    longest_name = max(name)

    id_ = []
    for row in table:
        if longest_name == len(row[1]):
            id_.append(row[0])

    theid = []        
    for word in id_:
        theid.append(word)
    
    thenameandid = []
    for row in table:
        for tableid in theid:
            if tableid == row[0]:
                thenameandid.append("ID: " + tableid + "\n" + "Name : " + row[1] + "\n")


    return thenameandid
# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """
    emails_and_names = []

    for elements in table:
        if elements[3] == str(1):
            emails_and_names.append(elements[2] + " ; " + elements[1])
    
    return emails_and_names