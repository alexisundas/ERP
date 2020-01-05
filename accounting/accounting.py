""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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
                      "Maximum Profit (year)",
                      "Average profit (year)",
                      "Back to main menu"]
                    
    ui.print_menu("Store Menu", menu_for_store, "Exit program")
    
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("accounting/items.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("accounting/items.csv"))
    elif option == "3":
        id_ = ui.get_inputs(["Enter the ID to be Removed:  "], "")
        remove(data_manager.get_table_from_file("accounting/items.csv"), id_)
    elif option == "4":
        id_ = ui.get_inputs(["Enter the ID to be Updated:  "], "")
        update(data_manager.get_table_from_file("accounting/items.csv"), id_)
    elif option == "5":
        result = which_year_max(data_manager.get_table_from_file("accounting/items.csv"))
        label = "The year with the highest profit : "
        ui.print_result(result,label)
        ui.get_inputs(["(0) Main Menu : \n"],"")
    elif option == "6":
        year = ui.get_inputs(["Average profit of the which year? : "],"")
        result = avg_amount(data_manager.get_table_from_file("accounting/items.csv"), year)
        label = f"Average profit of {year[0]} :"
        ui.print_result(result,label)
        ui.get_inputs(["(0) Main Menu : \n"],"")



def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]

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
    new_list_to_add.extend(ui.get_inputs(["Please add the Month of the transaction: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the Day of the transaction: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the Year of the transaction: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the Amount of the transaction: "],"")) #Nem lehet INT beirni a CSVbe szoval valamit kell nezni. INT KERNI ES UTANA ATIRNI STRINGRE
    table.append(new_list_to_add) # hozzáadni a csv filehoz
    data_manager.write_table_to_file("accounting/items.csv", table)

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

    common.toremoveid("accounting/items.csv",data_manager.get_table_from_file("accounting/items.csv"),id_)


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
            i[1] = ui.get_inputs(["Please add the new Month of the transaction: "],"")
            i[2] = ui.get_inputs(["Please add the new Day of the transaction: "],"")
            i[3] = ui.get_inputs(["Please add the new Year of the transaction: "],"")
            i[4] = ui.get_inputs(["Please add the new Amount of the transaction: "],"")
    data_manager.write_table_to_file("accounting/items.csv", table)

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    allyears = []
    for year in table:
        allyears.append(year[3])

    dic = {}
    for row in table:
        if row[3] not in dic.keys():
            dic[row[3]] = 0
        elif row[3] in dic.keys():
            if "in" == row[4]:
                dic[row[3]] += int(row[5])
            elif "out" == row[4]:
                dic[row[3]] -= int(row[5])
    profit = []
    
    for k,v in dic.items():
        profit.append(int(v))

    themaxprofit = max(profit)

    theprofityear = []
    for k,v in dic.items():
        if themaxprofit == int(v):
            theprofityear.append(k)
    

    return int(theprofityear[0])

def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    sum_profit = 0
    sum_item_count = 0

    try: 
        for line in table:
            if line[3] == year[0]:
                sum_item_count += 1
                if line[4] == "in":
                    sum_profit += int(line[5])
                else:
                    sum_profit -= int(line[5])
        return sum_profit / sum_item_count
    except ZeroDivisionError:
        ui.print_error_message("This give year is not in our Database")
