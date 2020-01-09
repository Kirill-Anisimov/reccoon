import service
import sqlite3


# Establish connection to the database
def create_db():
    try:
        sqlite_connection = sqlite3.connect('SQLite_Python.db')

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


# Create table FileNames in the database
def create_table_file_names():
    try:
        sqlite_connection = sqlite3.connect('SQLite_Python.db')
        sqlite_create_table_query = '''CREATE TABLE FileNames (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    rows INTEGER);'''

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


# Select list of file names uploaded to the system
def list_uploaded_file_names():
    try:
        sqlite_connection = sqlite3.connect('SQLite_Python.db')
        sqlite_select_file_names_query = '''SELECT name, rows from FileNames ORDER BY id'''

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_select_file_names_query)
        records = cursor.fetchall()

        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

    return records


# Select requested file name uploaded to the system
def select_my_filename(filename):
    try:
        sqlite_connection = sqlite3.connect('SQLite_Python.db')
        sqlite_select_file_names_query = 'SELECT name from FileNames WHERE name = "' + filename + '" ORDER BY id LIMIT 1'

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_select_file_names_query)
        link = cursor.fetchall()

        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
    return link


# Creates table from a query string
def create_random_table(query_string):
    try:
        sqlite_connection = sqlite3.connect('SQLite_Python.db')

        cursor = sqlite_connection.cursor()
        cursor.execute(query_string)
        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


# Creates a record about uploaded file to the FileNames table
def save_file_name(file):
    try:
        sqlite_connection = sqlite3.connect('SQLite_Python.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_query = 'INSERT INTO FileNames (name, rows) VALUES(' + '"{}"'.format(file) + ', ' + str(service.count_rows(file)) + ');'

        cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
