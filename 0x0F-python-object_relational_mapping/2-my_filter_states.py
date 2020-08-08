#!/usr/bin/python3
"""Module doc"""


if __name__ == "__main__":
    """
        Main function
    """

    import MySQLdb
    from sys import argv
    user_db = argv[1]
    pass_db = argv[2]
    name_db = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user_db,
                         passwd=pass_db,
                         db=name_db)

    cursor = db.cursor()
    query = "SELECT * \
             FROM BINARY states \
             WHERE name='{}' \
             ORDER BY id ASC".format(state_name)

    cursor.execute(query)
    data = cursor.fetchall()

    for states in data:
        print(states)

    cursor.close()
    db.close()
