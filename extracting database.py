import mysql.connector as db
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

print(databases_as_str)

'''idhu vandhu database ena laam irukku nu edukkum en pc la irukka mysql la irundhu
idhu rendu database irukku en pc la'''


'''adha remove pannavone naacreate panna database mattum irukkum , adhaan indha rendu'''








