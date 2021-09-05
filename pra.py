# get_data = int(input("Enter number"))
# factorial = 1

# if (get_data == 0):
#     print("The factorial of {} is 1".format(get_data))
# if (get_data<0):
#     print("The negative numbers doesnot support for factorial")
# else:
#     for number in range(1, get_data+1):
#         factorial = factorial*number
#     print("factorial of {} is".format(get_data),factorial)


# import sqlite3

# #Connecting to sqlite
# conn = sqlite3.connect('example.db')

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Doping EMPLOYEE table if already exists.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# #Creating table as per requirement
# sql ='''CREATE TABLE Student(
#    FIRST_NAME CHAR(20) NOT NULL,
#    LAST_NAME CHAR(20),
#    AGE INT,
#    SEX CHAR(1),
#    INCOME TEXT
# )'''
# cursor.execute(sql)
# print("Table created successfully........")

# # Commit your changes in the database
# conn.commit()

# #Closing the connection
# conn.close()


import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('example.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('''SELECT * from Student''')

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()


# import sqlite3

# #Connecting to sqlite
# conn = sqlite3.connect('example.db')

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# # Preparing SQL queries to INSERT a record into the database.
# cursor.execute('''INSERT INTO Student(
#    FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
#    ('Ramya', 'Rama Priya', 27, 'F', "9000")''')

# cursor.execute('''INSERT INTO Student(
#    FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
#    ('Vinay', 'Battacharya', 20, 'M', "6000")''')

# cursor.execute('''INSERT INTO Student(
#    FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
#    ('Sharukh', 'Sheik', 25, 'M', "8300")''')

# cursor.execute('''INSERT INTO Student(
#    FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
#    ('Sarmista', 'Sharma', 26, 'F', "10000")''')

# cursor.execute('''INSERT INTO Student(
#    FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES 
#    ('Tripthi', 'Mishra', 24, 'F', "6000 jhjfvdkjgfgdfiv  luiysdgfiug i iudgf ililugfi lugidlufg ieluefg li")''')

# # Commit your changes in the database
# conn.commit()
# print("Records inserted........")

# # Closing the connection
# conn.close()