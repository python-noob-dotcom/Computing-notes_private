import sqlite3, re

class Person:
    def __init__(self, full_name, dob):
        self.name = full_name
        self.dob = dob

    def is_adult(self):
        if 2024 - int(self.dob[:4]) > 18:
            return True
        else:
            return False
    
    def screen_name(self):
        return re.sub(r'[^\w\s+]', '', self.name + self.dob[5:]).replace(' ','')

class Staff(Person):
    def __init__(self, full_name, dob):
        super().__init__(full_name, dob)
    
    def screen_name(self):
        return super().screen_name() + 'Staff'\
    
    def is_adult(self):
        return True
    
class Student(Person):
    def __init__(self, full_name, dob):
        super().__init__(full_name, dob)
    
    def is_adult(self):
        return False
    
with sqlite3.connect(r'Computing-notes\Journey_to_A\Past Year Papers\2020 A level\school.db') as conn:
    cursor = conn.cursor()
    cursor.execute("BEGIN TRANSACTION")

    with open(r'Computing-notes\Journey_to_A\Past Year Papers\2020 A level\people.txt') as f:
        for line in f:
            line = line.strip().split(',')

            if line[2] == 'Person':
                p = Person(line[0], line[1])
            elif line[2] == 'Staff':
                p = Staff(line[0], line[1])
            else:
                p = Student(line[0], line[1])

            cursor.execute("INSERT INTO People(FullName, DateOfBirth, ScreenName, IsAdult) VALUES (?, ?, ?, ?)",
                           (p.name, p.dob, p.screen_name(), 0 if p.is_adult() == False else 1))
        
    conn.commit()


