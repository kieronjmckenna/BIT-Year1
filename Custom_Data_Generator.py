import csv
import random

# open files and create csv iterators
customer_file = open('Data/Customers.csv', 'r', newline='')
customer_reader = csv.reader(customer_file)
flower_file = open('Data/Flowers.csv', 'r', newline='')
flower_reader = csv.reader(flower_file)
transaction_file = open('Data/Transactions.csv', 'r', newline='')
transaction_reader = csv.reader(transaction_file)

# add data to lists

customer_list = []
[customer_list.append(item) for item in customer_reader]
flower_list = []
[flower_list.append(item) for item in flower_reader]
transaction_list = []
[transaction_list.append(item) for item in transaction_reader]

# set parameters for data to be generated

years = [2018, 2019, 2020]

number_flowers = len(flower_list)
number_customers = len(customer_list)
number_years = len(years)
number_months = 13
number_days = 29

number_orders_to_add = 200

max_flower_quantity = 20

# for to create specified amount of random orders
# for each sell order create a buy order of the same amount to keep stock unaffected but have data to analyze

for i in range(number_orders_to_add):
    year = years[random.randrange(number_years)]
    month = random.randrange(start=1, stop=number_months)
    day = random.randrange(start=1, stop=number_days)
    customer = customer_list[random.randrange(number_customers)][0]
    flower = flower_list[random.randrange(number_flowers)][0]
    quantity = random.randrange(max_flower_quantity)

    transaction_list.append(['Sell', customer, flower, quantity, day, month, year, 'Generated Sell Transaction'])
    transaction_list.append(['Buy', 'Daisy', flower, quantity, day, month, year, 'Generated Buy Transaction'])

# write new data to files


transaction_file = open(r'Data/Transactions.csv', 'w',
                        newline='')
transaction_writer = csv.writer(transaction_file)
[transaction_writer.writerow(row) for row in transaction_list]
