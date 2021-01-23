# Srape data with selenium from web site with javascript

### Background
Many modern sites are loaded with javascripts that add information to existing web page based on user actions. This type of sites sometimes dificult (if possible) to scrape using standard requests+beautifulsoup methods. This where python's `selenium` library can be used.

### Task descriptive
Objective of the scipt(s) was to scrape data from web site that contains registration data for public companies. Site has search page the load content after user enter search criteria(s). Initatials sraping with `requests` library returned empty page. Manual navigation over search results showed thousand of companies listed 10 per page.

Two script were used to collect and save data to CSV file. 

### Scraper.py
Python's library `selenium` used to utilize chromedriver for navigating through web pages.

```
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('creating webdriver..')
driver = webdriver.Chrome(executable_path='driver/chromedriver')

# create driver, navigate to page and get data
#driver = webdriver.Safari()
driver.get('https://core.cro.ie/search')
```
While method `.find_element_by_xpath()` find required tags on updaded page, another method `.click()` used to move to next page.
```
for page_num in range(10):
    cards = driver.find_elements_by_xpath(x_path_table)
    print('collecting data from page')
    for element in cards:
        file.writelines(element.text + '\n')
    time.sleep(5)
    driver.find_element_by_xpath(x_path_next).click()
    time.sleep(5)
```

### Export.py
After saving scraped data to CSV file, another scipt is used to format data to table. 

Python's library `Pandas` used for data manipulation
```
import pandas as pd

columns = ['Number' , 'Name', 'Type', 'Status', 'Registered On']

companies = []
company = {}

with open('companies.csv') as csv_file:
    for line in csv_file.readlines():
        if line.strip('\n') in columns:
            column = line.strip('\n')
            continue
        if line.strip('\n') == 'View Details':
            companies.append(company)
            company = {}
            continue
        company[column] = line.strip('\n')
        print(f'{column}: {company[column]}')
# create DataFrame
df = pd.DataFrame(companies).set_index('Number')
```
