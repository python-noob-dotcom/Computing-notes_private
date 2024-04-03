# Database Theory

## What are Databases?

Databases store data, holds information. <br>
    e.g. You are in charge of storing data in a library, you might set up a database that holds the information of books, patrons,
    people borrowing etc.

### Databases look similar to stuff like excel sheets, google spreadsheets, and ofc pandas DataFrames. But they are more powerful because

1. They can store more data
2. They can be secured using encryption
3. Multiple people can query to the database all at once

## The basics of Databases

### Tables

#### The main building block of Databases are tables, with rows and columns. Exactly the same as spreadsheets, DataFrames, Series, etc

1. Good habits in tables
    - Table names should be in lower case, should not include spaces, and refer to a collective group
    - The same thing for field names, just that field names should not be duplicated, and never share the same name as the table
    - Have as many tables as required, each with a clearly marked subject is better than having a general table
        - e.g. different sheets in excel or google spreadsheets for different things
2. Records
    - A record is a row in a table
    - A record holds data of a singzular observation (i.e. 1 set of independent and dependent variables)
3. Fields
    - A field is a column within a table, holding all the information about all observations about that field
4. Assigned seats
    - A unique identifier, for a singular record, like a key in a python dictionary that indentifies the singular item in the dictionary
        - e.g. `dict['key']`
