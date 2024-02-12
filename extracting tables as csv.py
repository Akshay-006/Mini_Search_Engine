import mysql.connector as db
import pandas as pd

tables=[]
databases_as_str=['pdf_to_text', 'search_engine']
amount_of_tables=0

connection=db.connect(
    host="localhost",
    user="root",
    password="password"
)

cursor=connection.cursor()

amount_of_db=len(databases_as_str)

def extract_tables_as_csv():
    counter=1
    global amount_of_tables
    for i in range(amount_of_db):
        connection.database=databases_as_str[i]

        cursor.execute("show tables;")

        result=cursor.fetchall()
        for table in result:
            a=''.join(map(str,table))
            query=f"select * from {a}"
            output=pd.read_sql(query,connection)
            output.to_csv(f"table{counter}.csv",index=False)
            counter+=1
            amount_of_tables+=1

extract_tables_as_csv()
#print(amount_of_tables)


'''
dict1={'id':1001,'name':'Tyler','Language':'English','Salary':10000.00}'''



'''indha maari dictionary create aaganum

adhu dhaan kashtamaa irukku panradhuku
'''














