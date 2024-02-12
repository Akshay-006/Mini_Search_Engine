amount_of_tables=2



for i in range(1,amount_of_tables+1):
    with open(f"table{i}.csv","r") as file:
        records=file.readlines()
        for record in records:
            fields=record.strip().split(',')






