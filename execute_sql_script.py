import mysql.connector
from mysql.connector import Error

def check_file_content(filename):
    """
    Check the content of the specified file and print it if it's not empty.
    
    Args:
    filename (str): The path to the file to check.
    """
    try:
        # Open and read the file content
        with open(filename, 'r') as file:
            content = file.read().strip()
            
            # Check if the file content is not empty
            if content:
                print("The file is not empty. Content:\n")
                print(content)
            else:
                print("The file is empty.")
                
    except FileNotFoundError:
        print(f"File not found: {filename}")

def execute_script_from_file(filename):
    """
    Execute SQL script from the specified file.
    
    Args:
    filename (str): The path to the SQL script file.
    """
    try:
        # Read the SQL script
        with open(filename, 'r') as file:
            sql_script = file.read()
            
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # Replace with your MySQL root password
            database='alx_book_store'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Execute the script
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

# Path to your SQL script
file_path = 'C:/Users/PC/.ipython/Intro_to_DB/database/task_2.sql'

# Check the file content
check_file_content(file_path)

# Execute the SQL script if the file is not empty
execute_script_from_file(file_path)
