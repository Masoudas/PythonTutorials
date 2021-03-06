"""
Me: Note that we generally don't want to fetch all the rows of the DB into memory. This is why we prefer to iterate over them. However, we may fetch them all after execution using the 'fetchall' function.

We’ll first illustrate the Result object more closely by making use of the rows we’ve inserted previously, running a textual SELECT statement on the table we’ve created. The object returned is called Result and represents an iterable object of result rows.

>>> with engine.connect() as conn:
...     result = conn.execute(text("SELECT x, y FROM some_table"))
...     for row in result:
...         print(f"x: {row.x}  y: {row.y}")

Result has lots of methods for fetching and transforming rows, such as the Result.all() method illustrated previously, which returns a list of all Row objects. It also implements the Python iterator interface so that we can iterate over the collection of Row objects directly.

The Row objects themselves are intended to act like Python named tuples. Below we illustrate a variety of ways to access rows. Me: But they are not actually any of them, and as such, need to be converted to them.

Tuple Assignment - This is the most Python-idiomatic style, which is to assign variables to each row positionally as they are received:

%%%%%%%%
result = conn.execute(text("select x, y from some_table"))
for x, y in result:
    # ...

%%%%%%
Integer Index - Tuples are Python sequences, so regular integer access is available too:
result = conn.execute(text("select x, y from some_table"))
  for row in result:
      x = row[0]

%%%%%%
Attribute Name - As these are Python named tuples, the tuples have dynamic attribute names matching the names of each column. These names are normally the names that the SQL statement assigns to the columns in each row. While they are usually fairly predictable and can also be controlled by labels, in less defined cases they may be subject to database-specific behaviors:

result = conn.execute(text("select x, y from some_table"))

for row in result:
    y = row.y

    # illustrate use with Python f-strings
    print(f"Row: {row.x} {row.y}")

%%%%%%%
Mapping Access - To receive rows as Python mapping objects, which is essentially a read-only version of Python’s interface to the common dict object, the Result may be transformed into a MappingResult object using the Result.mappings() modifier; this is a result object that yields dictionary-like RowMapping objects rather than Row objects:

result = conn.execute(text("select x, y from some_table"))
for dict_row in result.mappings():
    x = dict_row['x']
    y = dict_row['y']
"""
