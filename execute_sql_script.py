import mysql.connector
from mysql.connector import Error

def execute_script_from_file(filename):
    # Read the SQL script
    with open(filename, 'r') as file:
        sql_script = file.read()

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # replace with your MySQL root password
            database='alx_book_store'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Split the script into individual statements and execute them
            for result in cursor.execute(sql_script, multi=True):
                pass  # Execute the script statement by statement
            
            print("Script executed successfully")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Replace 'C:/path/to/task_2.sql' with the actual path to your SQL script
execute_script_from_file('C:/Users/PC/.ipython/Intro_to_DB/database/task_2.sql')
