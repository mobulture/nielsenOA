#Repo for Nielsen OA

The assignment is seperated into 3 files. One for database connection and queries, one for database population, and one for the GUI

Python 3.7 was used as the language for all files, with POSTGRESQL as the database hosted on AWS RDS
A requirements.txt file is included, the only non python standard library used is psycopg2. Other libraries used include csv for sample data parsing, and tkinter for GUI creation.

The DBWork files includes credentials for authentication for a read-only role.

The database is intended to be populated by populating.py, which then will populate the database, allowing for GUI.py to explore the database

The GUI was created using tkinter, it allows for some basic querying of aggregate functions using criteria that the user can select. 
There are selections as to what the target data for your search will be, as well as criteria to group it by


To use, run gui.py via python gui.py on the command line or by running with an IDE, to enter search terms, select search options on drop down menus, and then enter valid terms, which are displayed in a box below the drop down menus.  **Enter search terms seperated by comma, entries are case and space sensitive, so do not add trailing spaces and make sure your capitalization matches that of the search terms**. Data that you can view is based off of the sample entries provided in the hirevue.
