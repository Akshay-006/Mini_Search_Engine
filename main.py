import mysql.connector as db
import pandas as pd

databases=[]
databases_as_str=[]

connection=db.connect(
    host="localhost",
    user="root",
    password="password"
)

cursor=connection.cursor()
cursor.execute("Show databases;")

all_database=cursor.fetchall()
for database in all_database:
    databases.append(database)

a1=('information_schema',)#indha 4 database vandhu mysql download pana automatic aa irukkum
b1=('mysql',)#sql files maari
c1=('performance_schema',)
d1=('sys',)

databases.remove(a1)
databases.remove(b1)
databases.remove(c1)
databases.remove(d1)

#so adha remove panradhuku mela remove commands
for i in databases:
    a=''.join(map(str,i))
    databases_as_str.append(a)

#print(databases_as_str)

tables=[]
amount_of_tables=0

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

person=[]
person1=[]

for i in range(1,amount_of_tables+1):
    with open(f'table{i}.csv','r') as file:
        records = file.readlines()
        key_list = records[0].strip().split(',')
        for record in records:
            person.append(record.split())




search_term=input("Enter the term you want to search : ")

for i in person:
    for x in i:
        a=list(map(str,x.split(',')))
        person1.append(a)


#combination=list(map(str,search_term.split(' ')))
#print(combination)


for i in person1:
    for x in i:

        if search_term.lower()==x.lower() or search_term==x:
            print(i)
            break
        elif search_term.upper()==x.upper():
            print(i)
            break

low_prior=['what','often','is','the','for','in','where','when','how','are','?','.','!','a','there','who','many','likes','like']



combination=list(map(str,search_term.split(' ')))

for i in low_prior:
    if i.lower() in combination or i in combination:
        combination.remove(i)
    elif i.upper() in combination:
        combination.remove(i)

print(combination)

for y in combination:
    for x in person:
        for i in x:
            if y.lower()==i.lower() or y==i:
                for ai in x:
                    print(ai,end=' ')


            elif y.upper()==i.upper():
                for bi in x:
                    print(bi,end=' ')



