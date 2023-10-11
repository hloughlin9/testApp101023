import os
import pandas as pd
from mysql.connector import Connect

# Azure MySQL Flexible Server connection parameters
host = 'tdc-test-120.mysql.database.azure.com'
user = 'hloughlin9'
password = 'Petergriffin8316'
database = 'gastropods'
port = 3306

# Establishing the connection
connection = Connect(host=host, user=user, password=password,
        database=database, port=port)

cursor = connection.cursor()

cursor.execute("USE gastropods;")

cursor.execute("SELECT * FROM champions ORDER BY season DESC LIMIT 5;")

tbl = cursor.fetchall()

tbl_df = pd.DataFrame(tbl)
tbl_df.columns = ['team','season','points','manager','skipper']

print(tbl_df.head(4))