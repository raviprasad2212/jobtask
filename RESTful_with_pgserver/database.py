import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="mydb", user='postgres', password='Ravi', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()


# cursor.execute("DROP TABLE IF EXISTS task")

# #Creating table as per requirement
# sql ='''CREATE TABLE task(
#    id int unique,
#    title varchar(20),
#    description text,
#    done boolean
# )'''
# cursor.execute(sql)
# print("Table created successfully........")
# conn.commit()
# #Closing the connection
# conn.close()