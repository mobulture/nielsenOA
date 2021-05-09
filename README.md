#Repo for Nielsen OA

The assignment is seperated into 3 files. One for database connection and queries, one for database population, and one for the GUI

Python 3.7 was used as the language for all files, with POSTGRESQL as the database hosted locally

A requirements.txt file is included, the only non python standard library used is psycopg2.

The DBWork files includes credentials for a hypothetical POSTGRESQL user authentication. 

The database is intended to be populated by populating.py, which then will populate the database, allowing for GUI.py to explore the database

The GUI was created using tkinter, it allows for some basic querying of aggregate functions using criteria that the user can select. 
There are selections as to what the target data for your search will be, as well as criteria to group it by
