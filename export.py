import pandas as pd

columns = ['Number' , 'Name', 'Type', 'Status', 'Registered On']

companies = []
company = {}

with open('companies.csv') as csv_file:
    for line in csv_file.readlines():
        if line.strip('\n') in columns:
            #print('found!')
            column = line.strip('\n')
            continue
        if line.strip('\n') == 'View Details':
            companies.append(company)
            company = {}
            continue
        company[column] = line.strip('\n')
        print(f'{column}: {company[column]}')
        #print(line.strip('\n'))

df = pd.DataFrame(companies).set_index('Number')
print(df.head())

df.to_csv('export.csv')