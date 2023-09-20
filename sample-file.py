from mysql.connector import Error
import mysql.connector

# Establish a connection
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='YOUR_DATABASE_NAME'
    )

    if connection.is_connected():
        #print(f'Connected to MySQL database: {connection.database}')

        # Perform database operations here

        try:
            cursor = connection.cursor()

            # Example query
            cursor.execute("SELECT * FROM your_table_name")

            # Fetch and print results
            records = cursor.fetchall()
            for record in records:
                print(record) 
                

        except Error as e:
            print(f"Error: {e}")

        finally:
            # Close the cursor
            if 'cursor' in locals():
                cursor.close()

except Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        #print('Connection closed.')
