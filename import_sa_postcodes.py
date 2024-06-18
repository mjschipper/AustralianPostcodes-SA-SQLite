
import pandas as pd
import sqlite3

# URL of the CSV file
url = 'https://raw.githubusercontent.com/matthewproctor/australianpostcodes/master/australian_postcodes.csv'

# Read CSV file directly from the URL
data = pd.read_csv(url)

# Filter rows where the state is 'SA'
filtered_data = data[data['state'] == 'SA']

# Create a new SQLite database
conn = sqlite3.connect('australian_postcodes.db')
c = conn.cursor()

# Create a table
c.execute('''
CREATE TABLE IF NOT EXISTS sa_postcodes (
    id INTEGER PRIMARY KEY,
    postcode TEXT,
    locality TEXT,
    state TEXT,
    long REAL,
    lat REAL,
    dc TEXT,
    type TEXT,
    status TEXT)
''')

# Insert the data into the table
filtered_data.to_sql('sa_postcodes', conn, if_exists='replace', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()

print('Data imported successfully into SQLite database.')
