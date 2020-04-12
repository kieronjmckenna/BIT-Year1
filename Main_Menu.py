from System.modules import *
import csv

# customer management, add customer, remove customer, list customers


# initialise the main menu
if __name__ == '__main__':

    while True:
        initial_greeting = input('''Hi Daisy, Welcome to the Flower Shop Software Main Menu\n
            Please select what you would like to do
            - Add Transaction(1)
            - Customer Management(2)
            - Flower Management(3)
            - View Current Inventory(4)
            - Data Analytics(5)
            - Exit the System (break)
            ''')
        if initial_greeting == '1':
            while True:
                # ask whether daisy is bringing flowers into the shop or selling them
                order_type_input = input('Are you buying(1) or selling flowers(2)')
                # logic to change input to buy or sell
                if order_type_input == '1':
                    order_type_input = 'Buy'
                    customer_name_input = 'Daisy'
                    break
                elif order_type_input == '2':
                    order_type_input = 'Sell'
                    list_customers()
                    customer_name_input = input('Please enter the customers name')
                    break
            # get flower name, number of flowers and the comment for the order
            list_flowers()
            flower_input = input('Please enter the flower')
            quantity_input = input('Please enter the quantity of flowers')
            comment_input = input('Please enter the order comment')
            day_input = input('Please enter the day (number)')
            month_input = input('Please enter the month(number)')
            year_input = input('Please enter the year (2018, 2019, 2020)')
            # transfer input data into modules.Transaction
            Transaction(order_type=order_type_input,
                        customer=customer_name_input,
                        flower=flower_input,
                        quantity=quantity_input,
                        comment=comment_input,
                        day=day_input,
                        month=month_input,
                        year=year_input).add()
        elif initial_greeting == '2':
            while True:
                # ask what daisy would like to do regarding the customer
                customer_menu = input('''What would you like to do?
                                        - Add Customer(1)
                                        - Choose a Customer Profile(2): View/Add Comments, Edit or Delete
                                        - Back to Main Menu(break)
                                        ''')
                if customer_menu == '1':
                    # adding a customer, get the name, number and gender
                    customer_name_input = input('Please enter the customers name')
                    customer_number_input = input('Please enter the customers number')
                    customer_gender_input = input('Please enter the customers gender - Male(1) Female(2)')
                    # transfer data to modules.Customer logic
                    Customer(name=customer_name_input,
                             number=customer_number_input,
                             gender=customer_gender_input).add()

                    print(customer_list)
                elif customer_menu == '2':
                    while True:
                        # call modules.list_customers to list all customers to help daisy choose from
                        list_customers()
                        # get the input for which customer's profile daisy would like to view

                        customer_selector = input('Please Select a Customer or type "break" to go back')
                        if customer_selector == 'break':
                            break
                        # check if the customer exists with modules.customer function
                        elif Customer(name=customer_selector).exists():
                            while True:

                                selected_customer = Customer(name=customer_selector)
                                # loop through the dict reader, if the value for key 'Name' == chosen customer print
                                # that rows information
                                selected_customer.show_details()
                                # initialize an instance of a customer comment, then use modules.CustomerComment to list
                                # only that customers comment
                                comment_instance = CustomerComment(selected_customer.name)
                                comment_instance.list_filtered()
                                # give options for what to do with this customer
                                profile_menu = input('''\nWhat would you like to do?
                                - Add a Comment to the customers Profile(1)
                                - Remove a Comment from the customers Profile(2)
                                - Edit the Customers Information (3)
                                - Delete the Customer(4) (including their comments, their transactions will remain)
                                - Go back (any other key)
                                ''')
                                # logic to decide which function to use from modules
                                if profile_menu == '1':
                                    comment_instance.add()
                                elif profile_menu == '2':
                                    comment_instance.remove()
                                elif profile_menu == '3':
                                    selected_customer.edit()
                                elif profile_menu == '4':
                                    #
                                    # This still requires comments for the customer to be deleted,
                                    # currently it only removes the customer from customer.csv
                                    #
                                    selected_customer.remove()
                                elif profile_menu == 'break':
                                    break
                        else:
                            print('That\'s not a customer, please type carefully')
                elif customer_menu == 'break':
                    break

        elif initial_greeting == '3':
            while True:
                # follows duplicate logic from option 2 with customers, only the text printed is different
                flower_menu = input('''What would you like to do?
                                        - Add Flower(1)
                                        - Choose a Flower Profile(2): View/Add Comments, Edit or Delete
                                        - Back to Main Menu(break)
                                        ''')
                if flower_menu == '1':
                    flower_name_input = input('Please enter the flowers name')
                    flower_price_input = input('Please enter the flowers price')
                    flower_description_input = input('Please enter the flowers description')
                    add_entered_customer = Flower(flower_name_input, flower_price_input,
                                                  flower_description_input).add()
                elif flower_menu == '2':
                    while True:
                        list_flowers()
                        flower_selector = input('Please Select a Flower or type break to go back')
                        if flower_selector == 'break':
                            break
                        else:
                            if Flower(flower_selector).exists():
                                while True:
                                    flower_instance = Flower(flower=flower_selector)
                                    comment_instance = FlowerComment(flower_instance.flower)

                                    flower_instance.show_details()
                                    comment_instance.list_filtered()

                                    profile_menu = input('''\nWhat would you like to do?
                                    - Add a Comment to the Flower(1)
                                    - Remove a Comment from the Flower(2)
                                    - Edit the Flower\'s information(3)
                                    - Delete the Flower(4) (including their comments, 
                                      transaction of this flower will remain, but inventory will be set to 0)
                                    - Go back (break)
                                    ''')
                                    if profile_menu == '1':
                                        comment_instance.add()
                                    elif profile_menu == '2':
                                        comment_instance.remove()
                                    elif profile_menu == '3':
                                        flower_instance.edit()
                                    elif profile_menu == '4':
                                        #
                                        # write code to make transaction to set flower level to 0, keeps transactions in
                                        # database

                                        flower_instance.remove()
                                    elif profile_menu == 'break':
                                        break
                            else:
                                print('That\'s not a customer, please type carefully')
                elif flower_menu == 'break':
                    break
        elif initial_greeting == '4':
            while True:
                flower_dict = stock_take()
                print('Your Inventory')
                print('Flower  Level')
                for key, value in flower_dict.items():
                    print(key, "  ", value)
                back_to_menu = input('Type break to go back to the main menu')
                if back_to_menu == 'break':
                    break
        elif initial_greeting == '5':
            while True:
                current_month = input('Please enter the current month')
                if current_month in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
                    break
            while True:
                current_year = input('Please enter the current year')
                if current_year in ['2018', '2019', '2020']:
                    break
            while True:
                analytics_menu = input('''What would you like to do?
                                          Show Your Best Customers (1)
                                          Show the Shops Revenue (2)
                                          Show the Best Selling Flowers (3)                ''')

                while True:
                    time_frame = input('Please enter either 1 month (1), 6 months (6), 1 year (12), all time (all)')
                    if time_frame in ['1', '6', '12', 'all']:
                        break
                if analytics_menu == '1':
                    while True:
                        best_customers(current_month=current_month, current_year=current_year, time_frame=time_frame)
                        break_input = input('Please type break to go back')
                        if break_input == 'break':
                            break
                elif analytics_menu == '2':
                    while True:
                        monthly_revenue(current_month=current_month, current_year=current_year, time_frame=time_frame)
                        break_input = input('Please type break to go back')
                        if break_input == 'break':
                            break
                elif analytics_menu == '3':
                    while True:
                        best_flowers(current_month=current_month, current_year=current_year, time_frame=time_frame)
                        break_input = input('Please type break to go back')
                        if break_input == 'break':
                            break

        elif initial_greeting == 'break':
            print('All data saved!')
            customer_file = open('Data/Customers.csv', 'w', newline='')
            customer_writer = csv.writer(customer_file)
            customer_comment_file = open('Data/Customer-Comments.csv',
                                         'w',
                                         newline='')
            customer_comment_writer = csv.writer(customer_comment_file)
            flower_file = open('Data/Flowers.csv', 'w', newline='')
            flower_writer = csv.writer(flower_file)
            flower_comment_file = open('Data/Flower-Comments.csv', 'w',
                                       newline='')
            flower_comment_writer = csv.writer(flower_comment_file)
            transaction_file = open(r'Data/Transactions.csv', 'w',
                                    newline='')
            transaction_writer = csv.writer(transaction_file)

            [customer_writer.writerow(row) for row in customer_list]
            [customer_comment_writer.writerow(row) for row in customer_comment_list]
            [flower_writer.writerow(row) for row in flower_list]
            [flower_comment_writer.writerow(row) for row in flower_comment_list]
            [transaction_writer.writerow(row) for row in transaction_list]
            break
