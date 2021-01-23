import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('creating webdriver..')

driver = webdriver.Chrome(executable_path='driver/chromedriver')

# create driver, navigate to page and get data
#driver = webdriver.Safari()
driver.get('https://core.cro.ie/search')
print('connected to webdriver, waiting AJAX to complete')
# wait for AJAX to complete
time.sleep(15)
#assert "Python" in driver.title

# locate button 'search'
x_path = "//main[@id='content']/cro-search[@class='ng-star-inserted']/div[@class='rs-global-content-wrapper']/div[@class='rs-advanced-search-container rs-sticky-container']/div[@class='row']/div[@class='col-lg-4']/aside[@class='rs-form-wrapper']/cro-company-search-form[@class='ng-star-inserted']/form[@class='ng-untouched ng-pristine ng-valid']/section[@class='d-flex flex-row rs-container rs-content rs-container-border justify-content-between']/regsys-reactive-button[2]/button[@class='rs-button btn btn-outline-primary']"

print('looking for button Search to click..')
driver.find_element_by_xpath(x_path).click()
print('waiting for page to update..')
time.sleep(10)

# get location of tables
x_path_table = "//main[@id='content']/cro-search[@class='ng-star-inserted']/div[@class='rs-global-content-wrapper']/div[@class='rs-advanced-search-container rs-sticky-container']/div[@class='row']/div[@class='col-lg-8 ng-star-inserted']/cro-company-search-result[@class='ng-star-inserted']/section[@class='rs-filtered-content rs-search-result ng-star-inserted']/div[@class='mat-table-container ng-star-inserted']/mat-table[@class='mat-table cdk-table mat-sort']/mat-row[@class='mat-row cdk-row d-block d-lg-flex flex-lg-row p-2 py-3 mt-2 p-lg-3 mt-lg-3 ng-star-inserted']"

x_path_next = "//button[@type='button' and @aria-label='Next Page']"

x_path_details = "/html/body[@class='undefined']/regsys-root/div[@class='rs-root']/div[@class='rs-content-wrapper']/div[@class='rs-main-wrapper collapsed']/main[@id='content']/cro-search[@class='ng-star-inserted']/div[@class='rs-global-content-wrapper']/div[@class='rs-advanced-search-container rs-sticky-container']/div[@class='row']/div[@class='col-lg-8 ng-star-inserted']/cro-company-search-result[@class='ng-star-inserted']/section[@class='rs-filtered-content rs-search-result ng-star-inserted']/div[@class='mat-table-container ng-star-inserted']/mat-table[@class='mat-table cdk-table mat-sort']/mat-row[@class='mat-row cdk-row d-block d-lg-flex flex-lg-row p-2 py-3 mt-2 p-lg-3 mt-lg-3 ng-star-inserted'][1]/mat-cell[@class='mat-cell cdk-cell buttons-cell d-block d-inline-block flex-lg-row flex-lg-grow-0 flex-lg-shrink-0 cdk-column-redirectCol mat-column-redirectCol ng-star-inserted']/regsys-reactive-button/button[@class='rs-button btn btn-outline-primary']"

file = open('companies.csv', 'a')

for page_num in range(10):

    cards = driver.find_elements_by_xpath(x_path_table)
    print('collecting data from page')
    for element in cards:
        print()
        print(element.text)
        file.writelines(element.text + '\n')
    
    #time.sleep(5)
    #driver.find_element_by_xpath(x_path_details).click()
    time.sleep(5)
    print('looking for next page to click..')
    driver.find_element_by_xpath(x_path_next).click()
    print('waiting for page to update..')
    time.sleep(5)

file.close()
driver.close()