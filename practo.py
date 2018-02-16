from tinydb import TinyDB,Query
from selenium import webdriver

db = TinyDB('urls.json')
db_docs = TinyDB('doc_urls.json')
CITIES = ['ahmedabad','cochin','aurangabad','bangalore','jodhpur','bhopal','delhi','chandigarh','chennai','coimbatore','bhubaneshwar',
'vapi','jaipur','indore','raipur','vijayawada','kolkata','hyderabad','jamnagar','tiruchirapally','kolhapur','calicut','lucknow','madurai',
'mumbai','mysore','nagpur','goa','baroda','pune','surat','vaizag','nasik','trivandrum']
# for a in CITIES:
    # db.insert({'name':a,'pages':0,'docs':0})

# print len(CITIES)
# City = Query()
# print len(db.search(City.pages == 0))
# k = db.update({'pages':10},City.name == 'ahmedabad')
# print k 
# print db.search(City.name == 'ahmedabad')


driver = webdriver.Firefox(executable_path='/home/dhruvshah/Downloads/geckodriver')
City = Query()
for a in CITIES:
    pages = 1 
    docs = 0
    while True:
        driver.get('https://www.practo.com/%s/doctors?page=%d' % (a,pages))
        elems = driver.find_elements_by_class_name('u-color--primary')
        if len(elems) == 0:
            break
        else:
            docs += len(elems)
            # doc_urls = [a.get_attribute('href') for a in elems]
            for elem in elems:
                db_docs.insert({'city':a,'url':elem.get_attribute('href'),'name':elem.text})
        pages += 1
    if pages>1:
        k = db.update({'pages':pages-1,'docs':docs},City.name == a)
    else:
        k = db.update({'pages':-1,'docs':-1},City.name == a)
