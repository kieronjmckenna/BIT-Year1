import csv
import matplotlib.pyplot as plt

# Anything that interacts with the CSV/Data Files is located in this file (modules.py)


# For reference during development to keep track of csv structures
# Customer_Fieldnames = ['Name', 'Number', 'Gender']
# Flower_Fieldnames = ['Flower', 'Price', 'Description']
# Transaction_FieldNames = ['Order Type', 'Customer', 'Flower', 'Quantity', [day, month, year(2018,2019,2020)],
# 'Transaction Comment']
# Customer_Comment_FieldNames = ['Customer', 'Comment']
# Flower_Comment_FieldNames = ['Customer', 'Comment']

# Format
# Store File in Variable
# Create Python.CSV iterator instance, please find documentation here https://docs.python.org/3/library/csv.html

customer_file = open('Data/Customers.csv', 'r', newline='')
customer_reader = csv.reader(customer_file)

customer_comment_file = open('Data/Customer-Comments.csv', 'r',
                             newline='')
customer_comment_reader = csv.reader(customer_comment_file)

flower_file = open('Data/Flowers.csv', 'r', newline='')
flower_reader = csv.reader(flower_file)

flower_comment_file = open('Data/Flower-Comments.csv', 'r',
                           newline='')
flower_comment_reader = csv.reader(flower_comment_file)

transaction_file = open('Data/Transactions.csv', 'r', newline='')
transaction_reader = csv.reader(transaction_file)

# Format
# Create empty list to store data from  file
# Use shorthand for loop to append each value to file

customer_list = []
[customer_list.append(item) for item in customer_reader]

customer_comment_list = []
[customer_comment_list.append(item) for item in customer_comment_reader]

flower_list = []
[flower_list.append(item) for item in flower_reader]

flower_comment_list = []
[flower_comment_list.append(item) for item in flower_comment_reader]

transaction_list = []
[transaction_list.append(item) for item in transaction_reader]
print(transaction_list)


# Function used for looping through customer file
# Print index 0 of customer file row, "Name"

def list_customers():
    print('Your Customers')
    for row in customer_list:
        print(row[0])


# Function used for looping through flower file
# Print index 0 of flower file row, "Flower"

def list_flowers():
    print('Your Flowers')
    for row in flower_list:
        print(row[0])


# FEATURE 3 - SHOW FLOWERS AND INVENTORY LEVELS
# Process:
# Create an Empty Dictionary
# If the order is type 'Buy' and the flower is not in the dictionary, make flower value = quantity
# If the order is type 'Buy' and the flower is in the dictionary, add the quantity to the value
# If the order is type 'Sell' and the flower is not in the dictionary, make the flower value = -quantity
# If the order is type 'Sell and the flower is not in the dictionary, subtract the order quantity from the value
#
# Return A dictionary in the format {flower name: Inventory Level}


def stock_take():
    flower_dict = {}
    for row in transaction_list:
        # type,customer,flower,quantity,day,month,year,comment
        if row[0] == 'Buy' and row[2] not in flower_dict:
            flower_dict[row[2]] = int(row[3])
        elif row[0] == 'Buy' and row[2] in flower_dict:
            flower_dict[row[2]] += int(row[3])
        elif row[0] == 'Sell' and row[2] not in flower_dict:
            flower_dict[row[2]] = -int(row[3])
        elif row[0] == 'Sell' and row[2] in flower_dict:
            flower_dict[row[2]] -= int(row[3])
    return flower_dict


# Class to create instances of a Customer in main menu
#
# parameters number and gender have default values set to none so that Customer.exists can be called anywhere in code
# without knowing the customer number or gender


class Customer:
    def __init__(self, name, number=None, gender=None):
        self.name = name
        self.number = number
        self.gender = gender

        # data cleaning, loop runs when instance is created to ensure data integrity in CSV filez

    # if print() is called on an instance of Customer it well return self.name

    def __str__(self):
        return self.name

    # clean data inputed into customer instance to ensure data integrity in Customer.csv

    def clean_data(self):
        while True:
            # Attempt to turn self.number into a number
            try:
                int(self.number)
            except ValueError:
                # If python throws an error
                self.number = input('The Customer phone number must be a number. Please reenter as a number')
            if self.gender == '1':
                self.gender = 'Male'
            elif self.gender == '2':
                self.gender = 'Female'
            else:
                self.gender = input('Please enter either a 1 for Male or 2 for female')

    # loop through the customer file and return True if index 0 of any row is equal to self.name

    def exists(self):
        for row in customer_list:
            if row[0].lower() == self.name.lower():
                return True

    # print customers details to terminal

    def show_details(self):
        print(f'''Customer Info:
              Name: {self.name}
              Number: {self.number}
              Gender: {self.gender}
              ''')

    # Part 1 of 2 for FEATURE 7 ADD CUSTOMER/REMOVE CUSTOMER

    def add(self):
        while True:
            # Run Customer.clean_data on current instance ensuring data is in correct format
            self.clean_data()
            # if the customer already exists give option to go back or retype the customer to be added
            if self.exists():
                add_different = input(f'''{self.name} already exists. Would you like to\n
                            -Add a different Name(1)
                            -Go Back to the menu(2)
                            ''')
                if add_different == '1':
                    new_name = input('Please enter the new customer name')
                    # change the customer instance's name to the new input
                    self.name = new_name
                elif add_different == '2':
                    break
            # otherwise add the customer to customer_list and alert user that the they have been added to the list
            # then give the option to add another customer
            else:
                customer_list.append([self.name, self.number, self.gender])
                print(f'{self.name} has been added to the database')
                add_another_question = input('''Would you like to add another customer to the database?
                                       -Yes (1)
                                       -No, take me back to menu(2)
                            ''')
                if add_another_question == '1':
                    # take new inputs for next customer to be added, then repeat the while loop
                    self.name = input('Please enter the customer name ')
                    self.number = input('Please enter the customers number ')
                    self.gender = input('Please enter the customers gender ')
                elif add_another_question == '2':
                    break

    # Part 1 of 2 for FEATURE 10 - EDIT CUSTOMER/FLOWER Information

    def edit(self):

        # initiate loop
        # find which part of the customer they would like to change

        while True:
            attribute_selector_options = ['1', '2', '3', 'break']
            attribute_selector = input('Would you like to edit their Name(1), Number(2), or Gender(3), back(any '
                                       'key)')
            if attribute_selector in attribute_selector_options:
                break
            else:
                print('Sorry not an option')
        if attribute_selector == '1':
            # input the customers new name, check if that name already exists
            # if not change the name, break
            # otherwise tell the user that name already exists and repeat the loop for inputting and changing
            while True:
                new_name = input('Please enter the new customer name')
                if not Customer(new_name).exists():
                    # loop through customer_list and change the name where name is equal to inputted name
                    for row in customer_list:
                        if row[0] == self.name:
                            row[0] = new_name
                            break
                    print(f'{self.name} successful changed to {new_name}')
                    break
                else:
                    print('That name is already in the database, please enter a different name')
        elif attribute_selector == '2':
            while True:
                # get input for new number
                new_number = input('Please enter a new 4 digit number')
                self.number = new_number
                # run Customer.clean_data to ensure that a 4 digit number has been entered
                self.clean_data()
                for row in customer_list:
                    if row[0] == self.name:
                        row[1] = new_number
                print(f'{self.name}\'s number successfully changed to {new_number} \n')
                break
        elif attribute_selector == '3':
            # loop through customer_list and for row with selected customer change get what ever it is not
            for row in customer_list:
                if row[0] == self.name:
                    if row[2] == 'Male':
                        row[2] = 'Female'
                    else:
                        row[3] = 'Male'
            print(f'Gender Successfully Switched')

    # Part 2 of 2 for FEATURE ADD CUSTOMER/REMOVE CUSTOMER

    def remove(self):
        while True:
            # check the
            security_check = input('Are you sure you want to remove this customer? Yes(1) or No(Any other key)')
            if security_check == '1':
                customer_iterator = 0
                for row in customer_list:
                    if row[0] != self.name:
                        del customer_list[customer_iterator]
                    customer_iterator += 1

                CustomerComment(self.name).remove_all_customer_comments()

                transaction_iterator = 0
                for row in transaction_list:
                    if row[1] == self.name:
                        del transaction_list[transaction_iterator]
                    transaction_iterator += 1

                print(f'{self.name} Successfully removed from the system')
                break
            else:
                print('Delete successfully aborted')
                break


# Class to create instances of a Flower in main menu
#
# parameters price and description have default values set to none so that Flower.exists can be called anywhere in
# code without knowing the flowers price or description


class Flower:
    def __init__(self, flower, price=None, description=None):
        self.flower = flower
        self.price = price
        self.description = description

    # if print() is called on an instance of Customer it well return self.name

    def __str__(self):
        return self.flower

    # clean data inputed into customer instance to ensure data integrity in Customer.csv

    def clean_data(self):
        while True:
            try:
                float(self.price)
                return True
            except ValueError:
                self.price = input('The Customer phone number must be a number. Please reenter as a number')

    # loop through the customer file and return True if index 0 of any row is equal

    def exists(self):
        for row in flower_list:
            if row[0].lower() == self.flower.lower():
                return True

    # print customers details to terminal

    def show_details(self):
        if (self.price is None) or (self.description is None):
            for row in flower_list:
                if row[0].lower() == self.flower.lower():
                    self.price = row[1]
                    self.description = row[2]
        print(f'''Customer Info:
              Name: {self.flower}
              Price: {self.price}
              Description: {self.description}
              ''')

    # Part 1 of 2 for FEATURE 8 ADD/REMOVE Flower

    def add(self):
        while True:
            self.clean_data()
            if self.exists():
                add_different = input(f'''{self.flower} already exists. Would you like to\n
                            -Add a different Flower(1)
                            -Go Back to the menu(any key)
                            ''')
                if add_different == '1':
                    new_flower = input('Enter that new flower name')
                    self.flower = new_flower
                else:
                    break
            else:
                flower_list.append([self.flower, self.price, self.description])
                print(f'{self.flower} has been added to the database')
                add_another_question = input('''Would you like to add another flower to the database?
                                       -Yes (1)
                                       -No, take me back to menu(2)
                            ''')
                if add_another_question == '1':
                    self.flower = input('Please enter the flower name ')
                    self.price = input('Please enter the flowers price ')
                    self.description = input('Please enter the flowers description ')
                elif add_another_question == '2':
                    break

    # Part 2 of 2 for FEATURE 10 - EDIT CUSTOMER/FLOWER Information

    def edit(self):
        while True:
            attribute_selector = \
                input('Would you like to edit the Flower Name(1), Price(2), or Description(3), back(any key)')
            if attribute_selector == '1':
                while True:
                    new_flower = input('Please enter the new flowers name')
                    if not Flower(new_flower).exists():
                        for row in flower_list:
                            if row[0] == self.flower:
                                row[0] = new_flower
                                break
                        print(f'{self.flower} successful changed to {new_flower}')
                        break
                    else:
                        print('That\'s already a name in the database')
            elif attribute_selector == '2':
                while True:
                    new_price = input('Please enter a new price')
                    self.price = new_price
                    self.clean_data()
                    for row in flower_list:
                        if row[0] == self.flower:
                            row[1] = self.price
                    print(f'{self.flower}\'s price successfully changed to {new_price} \n')
                    break
            elif attribute_selector == '3':
                new_description = input('Please enter the new description of the flower')
                for row in flower_list:
                    if row[0] == self.flower:
                        row[2] = new_description
                print(f'Description of {self.flower} changed')
                break
            else:
                break

    # Part 2 of 2 for FEATURE ADD/REMOVE Flower

    def remove(self):
        while True:
            security_check = input('Are you sure you want to remove this flower? Yes(1) or No(Any other key)')
            if security_check == '1':
                for row in flower_list:
                    if row[0] == self.flower:
                        flower_list.remove(row)
                FlowerComment.remove_all_flower_comments(self.flower)

                transaction_iterator = 0
                for row in transaction_list:
                    if row[2] == self.flower:
                        del transaction_list[transaction_iterator]
                    transaction_iterator += 1
                print(f'{self.flower} successfully removed from the system')
                break
            else:
                break


# class to create instances of comments to be attached to customer profiles
#
#


class CustomerComment:
    def __init__(self, customer, comment=None):
        self.customer = customer
        self.comment = comment

    def add(self):

        self.comment = input('Please enter the comment to be added on the profile')
        customer_comment_list.append([self.customer, self.comment])
        print(f'Comment added to {self.customer}\'s profile')

    def remove(self):
        comment_number_input = int(
            input('From the profile above, please select which comment you would like to remove (By Number)'))
        specific_customer_comment_counter = 0
        for row in customer_comment_list:
            if row[0] == self.customer:
                specific_customer_comment_counter += 1
                if specific_customer_comment_counter == comment_number_input:
                    selected_comment = row[1]
                    customer_comment_list.remove(row)
                    break

    def remove_all_customer_comments(self):
        for row in customer_comment_list:
            if row[0] == self.customer:
                customer_comment_list.remove(row)

    def list_filtered(self):
        print('Comments')
        comment_counter = 1
        for row in customer_comment_list:
            if row[0] == self.customer:
                print(f"{comment_counter} - {row[1]}")
                comment_counter += 1


class FlowerComment:
    def __init__(self, flower, comment=None):
        self.flower = flower
        self.comment = comment

    def add(self):
        self.comment = input('Please enter the comment to be added on the profile')
        flower_comment_list.append([self.flower, self.comment])
        print(f'Comment added to {self.flower}\'s profile')

    def remove(self):
        comment_number_input = int(
            input('From the profile above, please select which comment you would like to remove (By Number)'))
        specific_customer_comment_counter = 0
        for row in flower_comment_list:
            if row[0] == self.flower:
                specific_customer_comment_counter += 1
                if specific_customer_comment_counter == comment_number_input:
                    flower_comment_list.remove(row)
                    break

    def remove_all_flower_comments(self):
        for row in flower_comment_list:
            if row[0] == self.flower:
                flower_comment_list.remove(row)

    def list_filtered(self):
        print('Comments')
        comment_counter = 1
        for row in flower_comment_list:
            if row[0] == self.flower:
                print(f"{comment_counter} - {row[1]}")
                comment_counter += 1


class Transaction:
    def __init__(self, order_type, customer, flower, quantity, comment,
                 day, month, year):
        self.order_type = order_type
        self.customer = customer
        self.flower = flower
        self.quantity = quantity
        self.date = [day, month, year]
        self.comment = comment

    def clean_data(self):
        while True:
            clean = False
            try:
                self.quantity = int(self.quantity)
                clean = True
            except ValueError:
                self.quantity = input('The order quantity must be a number. Please reenter as a number')
            try:
                self.date[0] = int(self.date[0])
                assert self.date[0] in range(1, 31)
                clean = True
            except AssertionError:
                self.date[0] = input('Please enter the day as an integer between 1 and 31')
            except ValueError:
                self.date[0] = input('Please enter the day as an integer between 1 and 31')
                clean = True
            try:
                self.date[0] = int(self.date[0])
                assert self.date[1] in range(1, 12)
                clean = True
            except AssertionError:
                self.date[1] = input('Please enter the month as an integer between 1 and 12')
            except ValueError:
                self.date[1] = input('Please enter the month as an integer between 1 and 12')
            try:
                self.date[2] = int(self.date[2])
                assert self.date[2] in range(2018, 2020)
                clean = True
            except AssertionError:
                self.date[2] = input('Please either enter 2018, 2019, 2020')
            if clean:
                break

    def __str__(self):
        return self.customer, self.flower, self.quantity, self.date

    def add(self):
        while True:
            flower_dict = stock_take()
            if self.order_type == 'Sell':
                if Flower(flower=self.flower).exists():
                    if Customer(name=self.customer).exists():
                        self.clean_data()
                        if flower_dict[self.flower] - self.quantity >= 0:
                            transaction_list.append(['Sell',
                                                     self.customer,
                                                     self.flower,
                                                     self.quantity,
                                                     self.date[0], self.date[1], self.date[2], self.comment])
                            print(f'{self.quantity} {self.flower} sold to {self.customer}')
                            break
                        else:
                            not_enough_question = input(f'''There\'s only {flower_dict[self.flower]} in the inventory
                                                            Would you Like to
                                                            - Lower the quantity(1)
                                                            - Cancel the Transaction(2)
                                                        ''')
                            if not_enough_question == '1':
                                while True:
                                    new_quantity = int(input(f'How many would you like to change to?'
                                                             f'(Max of {flower_dict[self.flower]})'))
                                    if new_quantity <= flower_dict[self.flower]:
                                        transaction_list.append(['Sell',
                                                                 self.customer,
                                                                 self.flower,
                                                                 new_quantity,
                                                                 self.date[0], self.date[1], self.date[2],
                                                                 self.comment])
                                        print(f'{new_quantity} {self.flower}s sold to {self.customer}')
                                        break
                                    else:
                                        print('You dont have enough of those to sell')
                            elif not_enough_question == '2':
                                break
                    else:
                        while True:
                            customer_question = input(f'''{self.customer} doesn\'t exist in the database
                                                          Please Retype carefully
                                                      ''')
                            if Customer(customer_question).exists():
                                self.customer = customer_question
                                break
                else:
                    while True:
                        flower_question = input(f'''{self.flower} doesn\'t exist in the database
                                                Would you like to:
                                                -Retype the Flower Name (1)
                                                - Pick a new flower
                                                ''')
                        if flower_question == '1':
                            list_flowers()
                            new_flower_question = input('Please enter the new flower name')
                            if Flower(new_flower_question).exists():
                                self.flower = new_flower_question

            # insert code saying the there isn't enough of the new flower to sell to the customer - offer to change
            # quantity of change the flower

            else:
                if Flower(self.flower).exists():
                    transaction_list.append(['Buy',
                                             'Daisy',
                                             self.flower,
                                             self.quantity,
                                             self.date[0], self.date[1], self.date[2],
                                             self.comment])
                    print(f'{self.quantity} of {self.flower} bought')
                    break
                else:
                    buy_flower_question = input(f'''{self.flower} is not in the data base 
                                                        Please add the flower before adding a transaction
                                                        -type 1 to go back to the menu
                                                        -or retype the flower name
                                                    ''')
                    if buy_flower_question == '1':
                        break
                    else:
                        self.flower = buy_flower_question


# shows the customers who have spent the most in the shop

def flower_price_dict():
    flower_price_dict_var = {}

    # loop through flower file to save price to dict in format {flower: price}

    for row in flower_list:
        flower_price_dict_var[row[0]] = row[1]
    return flower_price_dict_var


# Function used to filter transactions for all of the data analytics functions.

def type_date_filter(transaction_row, current_month, current_year, time_frame):
    # get current month and year for purpose of displaying data
    current_year_month = [int(current_month), int(current_year)]
    year_month_to_filter = [int(transaction_row[5]), int(transaction_row[6])]

    # Boolean that is returned by the function. For loops are used in Best_Customer, Best_Flowers and Revenue and only
    # return transaction rows that return true

    filter_boolean = False

    # dictionary used for the purpose of changing negative numbers to corresponding months.
    # For example - If 6 months (time_frame) is chosen and the current month is said to be 1/2020, this dictionary will
    # convert 1, 0, -1, -2, -3, -4, -5 to 1, 12, 11, 10, 9, 8 or 1/2020, 12/2019, 11/2019, 10,2019, 9/2019 ,8/2019 in
    # this case
    month_convert_dict = {
        0: 12,
        -1: 11,
        -2: 10,
        -3: 9,
        -4: 8,
        -5: 7,
        -6: 6,
        -7: 5,
        -8: 4,
        -9: 3,
        -10: 2,
        -11: 1
    }

    # Only allow transaction rows with type sell.
    if transaction_row[0] == 'Sell':
        # Correspond filtering to selected time frame
        if time_frame == '1':
            # If time frame selected is 1 month, only return transaction_rows of the same month and year
            if (current_year_month[0] == year_month_to_filter[0]) and \
                    (current_year_month[1] == year_month_to_filter[1]):
                filter_boolean = True
        elif time_frame == '6':
            # empty list instantiated for the purpose of appending months that fit the time frame criteria corresponding
            # to the users selected month and year
            date_month_list = []

            # variable used for keeping track of iterations
            i = 0

            # do 6 iterations as time frame selected is 6 months

            for month in range(6):
                # instantiate variables to keep track of months to add
                iterated_month = current_year_month[0] - i
                iterated_year = current_year_month[1]

                # if iterated month is in dictionary month_convert_dict then it is in the year before.
                # The dictionary is used to convert iterated month to the corresponding value
                # the iterated year is changed to the year before

                if iterated_month in month_convert_dict:
                    iterated_month = month_convert_dict[iterated_month]
                    iterated_year = current_year_month[1] - 1

                # add the month to the list, meaning any transaction_rows with this month and year will not be filtered
                date_month_list.append([iterated_month, iterated_year])

                # add 1 to the iteration variable meaning iterated_month will evaluate to one less than the previous
                # iteration

                i += 1

            # logic to say filter any transaction_row that is in the time frame specified
            if year_month_to_filter in date_month_list:
                filter_boolean = True

        elif time_frame == '12':
            # Please see the immediate previous elif statement "elif time_frame == '6'". Code is duplicated except for
            # range. Function could have been created however we decided legibility would have been impacted
            date_month_list = []
            i = 0
            for month in range(12):
                iterated_month = current_year_month[0] - i
                iterated_year = current_year_month[1]
                if iterated_month in month_convert_dict:
                    iterated_month = month_convert_dict[iterated_month]
                    iterated_year = current_year_month[1] - 1
                date_month_list.append([iterated_month, iterated_year])
                i += 1
            if year_month_to_filter in date_month_list:
                filter_boolean = True
        elif time_frame == 'all':
            # Determine if month and year in transaction row are less than current_month and current_year
            if (year_month_to_filter[1] <= current_year_month[1]) \
                    and (year_month_to_filter[0] <= current_year_month[0]):
                filter_boolean = True
        # Depending on which time has been specified this return statement will determine if the transaction row is
        # added to the filtered list
        return filter_boolean

    # Else staement corresponds to Transaction Type, if its not 'Sell' and is therefore 'Buy' it will not need to be
    # analyzed

    else:
        return False


def best_customers(current_month, current_year, time_frame):
    # Instanciate a dictionary to keep track of customers and the sum of each persons purchases
    customer_total_purchase_dict = {}

    # make use of function flower_price_dict, the dictionary returned by this function will then be stored in
    # flower_dict
    # format {flower name: price}
    # this is needed to calculate the total of each order as each flowers price is not stored in the transaction file
    # in order to avoid data redundancy

    flower_dict = flower_price_dict()

    # loop through all the transactions

    # makes use of type_date_filter - short hand for loop to say write row to new instantiated variable only if when
    # row is passed in for parameter transaction_row type_date_filter returns True with current specifications for
    # current_month, current_year, time_frame
    time_filtered_transaction_list = \
        [row for row in transaction_list if type_date_filter(transaction_row=row,
                                                             current_month=current_month,
                                                             current_year=current_year,
                                                             time_frame=time_frame)]

    for transaction_row in time_filtered_transaction_list:

        # type,customer,flower,quantity,day,month,year,comment

        # only deal with sell transactions

        # store total of the order (price * quantity) in variable order sum
        order_sum = float(flower_dict[transaction_row[2]]) * int(transaction_row[3])

        # if the customer isn't in the dictionary yet (first transaction with this customer iterated) set the
        # dictionary value equal to sum, otherwise (not first transaction iterated) add order_sum to value of dictionary
        # key which has a value of the customers name

        if transaction_row[1] not in transaction_list:
            customer_total_purchase_dict[transaction_row[1]] = order_sum
        else:
            customer_total_purchase_dict[transaction_row[1]] += order_sum

    # create new list to append dictionary key and values for the purpose of having a way to
    # sort before seperating into two lists
    # necessary as python dictionaries are inherently unordered and cannot be put into a specific order

    customer_total_purchase_list = []

    for key, value in customer_total_purchase_dict.items():
        customer_total_purchase_list.append([key, value])

    # parameter key of built in function 'sort' requires function to pass in each item iterated, then will sort by
    # returned values, in this case its item 2 in list (sum of orders) in reverse to provide in descending order for
    # bar chart

    def sort_second(val):
        return val[1]

    customer_total_purchase_list.sort(key=sort_second, reverse=True)

    # create two more lists for purpose of passing into x and y axis of plt.bar

    customer_sorted_list = []
    price_sorted_list = []

    # iterate list that is now in descending order and split into seperate lists for purpose of bar chart
    for item in customer_total_purchase_list:
        customer_sorted_list.append(item[0])
        price_sorted_list.append(item[1])
    plt.bar(customer_sorted_list, price_sorted_list)
    plt.show()


def monthly_revenue(current_month, current_year, time_frame):
    # dictionary instantiated for thee purposes of keeping track of sum of each month

    monthly_revenue_dict = {}

    # dictionary retured by function flower_price_dict again stored in variable for purposed of calculating order sums
    flower_dict = flower_price_dict()

    # Please see comment in def Best_Customers where the same statement is used to filter transaction rows
    time_filtered_transaction_list = \
        [row for row in transaction_list if type_date_filter(transaction_row=row,
                                                             current_month=current_month,
                                                             current_year=current_year,
                                                             time_frame=time_frame)]

    # built in python function parameter takes function that it passes each iteration into. It then sorts based on the
    # returned values
    #
    # month_total_list is in format: [month/year string, [months order sum, month int, year int]]
    # therfore returned values at index [1][1] will target the month int    ^^^^^^^^
    def sort_by_month(val):
        return val[5]

    # month_total_list is in format: [month/year string, [months order sum, month int, year int]]
    # therfore returned values at index [1][1] will target the year int                ^^^^^^^^
    def sort_by_year(val):
        return val[5]

    # sort by the returned values of sort_by_year
    #
    # Sorting by month first puts months in position and then sorts by year, moving the lists into years already with
    # correct month order
    #
    # In other words sorting by year last overrides the order of month where needed, but sorting by month last would
    # take priority over the continuity of years

    # sort by the returned values of sort_by_month
    # loop through now filtered transaction rows

    for transaction_row in time_filtered_transaction_list:
        # calculate the sum of the order

        order_sum = float(flower_dict[transaction_row[2]]) * int(transaction_row[3])

        # This string is created for two purposes. First we attempted to use "for in" logic on a dictionary with keys
        # in the format [month, year]. However python did not allow this.
        #
        # Therefore strings are created to serve as keys in the dictionary.
        #
        # These strings are later repurposed to be placed underneath corresponding data points

        year_month_string = transaction_row[5] + '/' + transaction_row[6]

        # logic -> check if month/year string is not in the dictionary - if so store the order, sum, month and year
        # in the key's value as a list (month and year are stored again as integers for the purpose of sorting)
        # otherwise just add the current orders sum to the months value at list index 0
        if year_month_string not in monthly_revenue_dict:
            monthly_revenue_dict[year_month_string] = order_sum
        else:
            monthly_revenue_dict[year_month_string] += order_sum

    # Instantiate two lists for the purpose of values to plot (plt.plot) and to show time frame with the month names
    # (plt.xticks)

    month_title_list = []
    month_revenue_list = []
    # append key and value of dictionary to instantiated list
    for key, value in monthly_revenue_dict.items():
        month_title_list.append(key)
        month_revenue_list.append(value)

    # plt.xticks takes,  for our purposes, parameters ticks and labels. Ticks specifies 'A list of positions at which
    # ticks should be placed.'
    #
    # Therefore below we create a list of incrementing integers to correspond with the length of the list of months to
    # evenly space month labels across the graph
    #
    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.xticks.html

    months = len(month_revenue_list)
    int_list = []
    i = 0
    for x in range(months):
        int_list.append(i)
        i += 1

    # plot calculated sums of orders per month
    plt.plot(month_revenue_list)
    plt.xticks(int_list, month_title_list, rotation='vertical')
    plt.xlabel('Months Selected')

    plt.ylabel('Revenue')
    plt.title(f'Revenue Last {str(months)} Months')
    plt.show()


def best_flowers(current_month, current_year, time_frame):
    # again instantiate dictionary to get prices of flowers

    flower_dict = flower_price_dict()

    # instantiate dictionary to store flowers and their sales per month

    flower_month_dict = {}

    # filter transaction rows to specified time frame and current month and year. Please see Best_Customers for further
    # explanation of logic

    time_filtered_transaction_list = \
        [row for row in transaction_list if type_date_filter(transaction_row=row,
                                                             current_month=current_month,
                                                             current_year=current_year,
                                                             time_frame=time_frame)]

    def sort_by_month(val):
        return int(val[5])

    def sort_by_year(val):
        return int(val[6])

    time_filtered_transaction_list.sort(key=sort_by_month)
    time_filtered_transaction_list.sort(key=sort_by_year)
    # iterate filtered transaction rows
    for transaction_row in time_filtered_transaction_list:

        # type,customer,flower,quantity,day,month,year,comment

        # store total of the order (price * quantity) in variable order sum
        order_sum = float(flower_dict[transaction_row[2]]) * int(transaction_row[3])

        year_month_string = transaction_row[5] + '/' + transaction_row[6]
        # check if the flower name is in the dictionary
        # if it isnt set it equal to a dict format {flower: {month: sum}}
        # if it is check if value from year/month from transaction has been logged, if not add
        # {month: {sum, month, year}} to flowers dict
        # other wise add the order sum to the value\

        if transaction_row[2] not in flower_month_dict:
            flower_month_dict[transaction_row[2]] = \
                {year_month_string: order_sum}
        else:
            if year_month_string not in flower_month_dict[transaction_row[2]]:
                flower_month_dict[transaction_row[2]][year_month_string] = \
                    order_sum
            else:
                flower_month_dict[transaction_row[2]][year_month_string] += order_sum

    # instantiate list to store month/year strings to place on xticks

    month_list = []

    int_list = []
    i = 0

    first_iteration = 0
    for flower, month_sum in flower_month_dict.items():
        plt.annotate(flower, xy=(0, list(month_sum.values())[0]))
        flower_sum_list = []
        for month, sum_for_month in month_sum.items():
            if first_iteration == 0:
                month_list.append(month)
            flower_sum_list.append(sum_for_month)

        first_iteration += 1

        plt.plot(flower_sum_list)

    for x in range(len(month_list)):
        int_list.append(i)
        i += 1

    plt.xticks(int_list, month_list, rotation='vertical')
    plt.ylabel('Flower Sales')
    plt.xlabel('Months')
    plt.show()
