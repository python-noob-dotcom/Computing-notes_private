import sqlite3 

with sqlite3.connect('./equipment.db') as conn:
    cursor = conn.cursor()
    location = input('What devices do you want from which office?: ')
    statement = "SELECT D.serial_number, Type, Location FROM Device AS D WHERE D.Location = ?"
    res = cursor.execute(statement, (location,)).fetchall()

    print(f"{'Serial Number':<15} | {'Type':<15} | {location:<15}")
    print('_'*70)
    for result in res:
        print(f'{result[0]:<15} | {result[1]:<15} | {result[2]:<15}')