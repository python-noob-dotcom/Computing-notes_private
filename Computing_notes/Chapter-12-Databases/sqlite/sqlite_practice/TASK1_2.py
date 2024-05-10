import sqlite3

with open('./LAPTOPS.txt') as laptops:
    laptop = laptops.read().split('\n')

with open('./MONITORS.txt') as monitors:
    monitor = monitors.read().split('\n')

with open('./PRINTERS.txt') as printers:
    printer = printers.read().split('\n')

with sqlite3.connect('./equipment.db') as conn:

    cur = conn.cursor()

    try:
        cur.execute('BEGIN TRANSACTION')
        statement = 'INSERT INTO Device (serial_number, type, model, location, date_of_purchase, written_off) VALUES (?, ?, ?, ?, ?, ?)'
        statement_monitor = 'INSERT INTO Monitor (serial_number, date_cleaned) VALUES (?, ?)'
        statement_laptop = 'INSERT INTO Laptop (serial_number, weight_kg) VALUES (?, ?)'
        statement_printer = 'INSERT INTO Printer (serial_number, toner, date_changed) VALUES (?, ?, ?)'

        for lap in laptop:
            lap = lap.split(',')
            lap.insert(1, 'Laptop')
            lap_2 = tuple(lap)[:6]
            cur.execute(statement, lap_2)
            cur.execute(statement_laptop, (lap[0], lap[6]))

        for mon in monitor:
            mon = lap.split(',')
            mon.insert(1, 'Monitor')
            mon_2 = tuple(mon)[:6]
            cur.execute(statement, mon_2)
            cur.execute(statement_monitor, (mon[0], mon[6]))

        for prin in printer:
            prin = lap.split(',')
            prin.insert(1, 'Printer')
            prin_2 = tuple(prin)[:6]
            cur.execute(statement, prin)
            cur.execute(statement_printer, (prin[0], prin[6], prin[7]))

        conn.commit()

    except sqlite3.Error:

        print('Sql error')
        conn.rollback()

    except:
        conn.rollback()