'''from random import choice

def randomstr():
    main = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string = ""

    for i in range(5):
        string += choice(main)

    results = db.execute("SELECT * FROM urls WHERE short = (?)", string)

    if results:
        randomstr()

    else:
        return string


randomstr()

'''

from cs50 import SQL

db = SQL("sqlite:///urls.db")

"""db.execute('''
    CREATE TABLE urls(
        id INTEGER PRIMARY KEY,
        short varchar(255) NOT NULL,
        long varchar(255) NOT NULL
    )
''')"""

print(db.execute("SELECT * FROM urls"))