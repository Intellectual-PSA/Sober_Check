import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')  # creates a database in RAM
        print(f'successful SQLite version: {sqlite3.version}')
    except Error as e:
        print(e)

    if conn:
        return conn


def create_table(conn):
    try:
        query = """CREATE TABLE IF NOT EXISTS DrugCheck (
                                                id integer PRIMARY KEY,
                                                resident_name text NOT NULL,
                                                check_date text,
                                                checked_by text,
                                                result text
                                            ); """
        conn.execute(query)
    except Error as e:
        print(e)


def add_check_result(conn, check_result):
    query = '''INSERT INTO DrugCheck(resident_name, check_date, checked_by, result)
              VALUES(?,?,?,?) '''
    conn.execute(query, check_result)


def main():
    # Establishing Connection
    conn = create_connection()

    # Creating Table
    create_table(conn)

    # Assuming check results
    check_results = [('John Doe', '2023-05-27', 'Officer A', 'No Drugs Found'),
                     ('Jane Doe', '2023-05-27', 'Officer B', 'Drugs Found'),
                     ('Jim Doe', '2023-05-27', 'Officer A', 'No Drugs Found')]

    # Adding check results to the database
    for check_result in check_results:
        add_check_result(conn, check_result)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
