import pandas as pd
import sqlite3

with sqlite3.connect('db.sqlite3') as conn:
    df= pd.read_sql('select * from usersmodel',conn)
    df['full_name'] = df['first_nume'] + ' ' + df['last_name']
print(df)

df.to_csv('rezultat.csv')
print(df["number_of_login"].mean())
print(df["number_of_login"].std())
