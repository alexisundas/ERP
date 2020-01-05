""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least PRICE special characters (except: ';'), PRICE number, PRICE lower and PRICE upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

ID = 0
TITEL = 1
PRICE = 2
MONTH = 3
DAY = 4
YEAR = 5

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
                      "Get Lowest Price Item ID",
                      "Get Items Sold Between Given Dates",
                      "Back to main menu"]
                    
    ui.print_menu("Store Menu", menu_for_store, "Exit program")
    
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("sales/sales.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("sales/sales.csv"))
    elif option == "3":
        id_ = ui.get_inputs(["Enter the ID to be Removed:  "], "")
        remove(data_manager.get_table_from_file("sales/sales.csv"), id_)
    elif option == "4":
        id_ = ui.get_inputs(["Enter the ID to be Updated:  "], "")
        update(data_manager.get_table_from_file("sales/sales.csv"), id_)
    elif option == "5":
        result = get_lowest_price_item_id(data_manager.get_table_from_file("sales/sales.csv"))
        label = "The lowest item's ID: "
        ui.print_result(result, label)
        ui.get_inputs(["(0)Main Menu "],"")
    elif option == "6":
        month_from = ui.get_inputs(["From Month: "],"")
        day_from = ui.get_inputs(["From Day: "],"")
        year_from = ui.get_inputs(["From Year: "],"")
        month_to = ui.get_inputs(["To the Month: "],"")
        day_to = ui.get_inputs(["To the Day: "],"")
        year_to = ui.get_inputs(["To the Year: "],"")
        result = get_items_sold_between(data_manager.get_table_from_file("sales/sales.csv"), month_from, day_from, year_from, month_to, day_to, year_to)
        show_table(result)
        
def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "Title" , "Price","Month","Day","Year"]

    ui.print_table(table, title_list)

    inputs = ui.get_inputs(["\n"], "")
    if inputs == ID:
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
    new_list_to_add.extend(ui.get_inputs(["Please add the Price: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the month: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the day: "],""))
    new_list_to_add.extend(ui.get_inputs(["Please add the year: "],""))
    
    table.append(new_list_to_add) # hozzáadni a csv filehoz
    data_manager.write_table_to_file("sales/sales.csv", table)

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

    common.toremoveid("sales/sales.csv",data_manager.get_table_from_file("sales/sales.csv"),id_)


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
        if i[ID] == id_:
            i[TITEL] = ui.get_inputs(["What should i update the titel to: "],"")
            i[PRICE] = ui.get_inputs(["What should I update the price to? "],"")
            i[MONTH] = ui.get_inputs(["What should I update the month to? "],"")
            i[DAY] = ui.get_inputs(["What should I update the day? "],"")
            i[YEAR] = ui.get_inputs(["What should I update the year? "],"")
    
    data_manager.write_table_to_file("sales/sales.csv", table)

    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    all_prices = []
    for row in table:
        if int(row[PRICE]) > ID:
             all_prices.append(int(row[PRICE]))

    min_price = min(all_prices)
    id_of_min = []

    for row in table:
        if int(row[PRICE]) == min_price:
            id_of_min.append(row[ID])
    
    unsorted_list = []

    for row in table:
        if row[ID] in id_of_min:
            unsorted_list.append(row[TITEL])
    
    sort_list = []

    for row in unsorted_list:
        if row == min(unsorted_list):
            sort_list.append(row)
    
    the_id = []
    for row in table:
        if sort_list[0] in row:
            the_id.append(row[ID])
    
    result = the_id[0]



    return result


    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    try : 
        from_date = []
        from_date.append(int(month_from[0]))
        from_date.append(int(day_from[0]))
        from_date.append(int(year_from[0]))

        to_date = []
        to_date.append(int(month_to[0]))
        to_date.append(int(day_to[0]))
        to_date.append(int(year_to[0]))

        NEWMONTH = 0
        NEWDAY = 1
        NEWYEAR = 2
    except ValueError:
        ui.print_error_message("No date given ")
        
    between_the_dates = []

    
    for row in table:
        if from_date[NEWYEAR] <= int(row[YEAR]) and from_date[NEWMONTH] < int(row[MONTH]) and from_date[NEWDAY] <= int(row[DAY]):
            between_the_dates.append(row)
        elif from_date[NEWYEAR] == int(row[YEAR]) and from_date[NEWMONTH] < int(row[MONTH]):
            between_the_dates.append(row)
        elif from_date[NEWYEAR] == int(row[YEAR]) and from_date[NEWMONTH] == int(row[MONTH]) and from_date[NEWDAY] <= int(row[DAY]):
            between_the_dates.append(row)
            
            '''if from_date[NEWYEAR] < int(row[YEAR]):
                if to_date[NEWYEAR] > int(row[YEAR]):
                    between_the_dates.append(row)
        elif from_date[NEWMONTH] <= int(row[MONTH]):
            if from_date[NEWMONTH] < int(row[MONTH]):
                if to_date[NEWMONTH] > int(row[MONTH]):
                    between_the_dates.append(row)
        elif from_date[NEWDAY] <= int(row[DAY]):
            if from_date[NEWDAY] < int(row[DAY]):
                if to_date[NEWDAY] > int(row[DAY]):
                        between_the_dates.append(row)'''
    """result = []
    for item in between_the_dates:
        result.append(",".join(item))

    realresult = "\n"+ "\n".join(result)"""


    return between_the_dates
