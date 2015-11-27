from selenium import webdriver
import time
freeRice = webdriver.Chrome()
freeRice.get('http://www.freerice.com')
time.sleep(1)
thesaurus = webdriver.Chrome()
thesaurus.get('http://www.thesaurus.com/')
count = 0
while True:
    question = freeRice.find_element_by_class_name('question-link').text
    search_field = thesaurus.find_element_by_class_name('search-input')
    search_field.send_keys(question.split(' ')[0])
    search_field.submit()
    synonyms_wrapper = thesaurus.find_element_by_class_name('synonyms_wrapper')
    options = freeRice.find_elements_by_class_name('answer-item')
    not_found = True
    for option in options:
        print option.text
        if option.text in synonyms_wrapper.get_attribute('innerHTML') and option.text != '':
            not_found = False
            option.click()
            break
    if not_found:
        options[0].click()
    time.sleep(3)
freeRice.close()
thesaurus.close()