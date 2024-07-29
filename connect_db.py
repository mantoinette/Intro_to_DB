import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='alx_book_store'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
        else:
            print("Connection failed.")
            return None

    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

def execute_sql_file(connection, file_path):
    try:
        cursor = connection.cursor()
        with open(file_path, 'r') as file:
            sql_script = file.read()
        # Split script into individual statements and execute each
        statements = sql_script.split(';')
        for statement in statements:
            if statement.strip():
                cursor.execute(statement)
                print(f"Executed: {statement.strip()[:50]}...")  # Log the first part of the statement
        connection.commit()
        print("SQL script executed successfully")
    except Error as e:
        print(f"Error while executing SQL script: {e}")
    finally:
        cursor.close()

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        execute_sql_file(conn, 'alx_book_store.sql')
        conn.close()
