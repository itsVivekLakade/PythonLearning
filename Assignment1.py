import mysql.connector

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test"
)

my_database = db_connection.cursor()

sql_statement = "SELECT * FROM users"
my_database.execute(sql_statement)

output = my_database.fetchall()
for x in output:
  print(x)
