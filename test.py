amount_of_tables=4
person=[]
person1=[]
result=[]

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


for i in person1:
    for x in i:
        if search_term.lower()==x.lower() or search_term==x:
            print(i)
        elif search_term.upper()==x.upper():
            print(i)

low_prior=['what','is','the','for','in','where','when','how','are','?','.','!','a']


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





#print(person)
#print(person1)


























