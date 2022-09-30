from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from bs4 import BeautifulSoup
import requests



options = Options()
options.headless = True
options.add_argument('start-maximized')

browser = webdriver.Chrome(r'C:\Users\haral\Documents\Programmering\Python\Chromedriver\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("headless")
##self.driver = webdriver.Chrome(executable_path=r'C:\Users\haral\Downloads\chromedriver.exe',options=options)



def finnfjell():
    fjellvalg=input('Hvilket fjell skal du på?  ')
    browser.get('https://ut.no/')
    sleep(0.3)
    søk=browser.find_element_by_id('input-field')
    søk.send_keys(fjellvalg)
    søk.send_keys(Keys.ENTER)
    sleep(0.5)
    
    cookie=browser.find_element_by_class_name('c-button')
    cookie.click()
    sleep(0.5)
    
    valg=browser.find_elements_by_class_name('explore-page-search__item-link')
    teller=1
    if len(valg)>5:
        for i in valg[:5]:
            print(teller,'-',i.text)
            teller+=1
        bruker=int(input('Du søkte "{}", hvilken tur tenker du på? (skriv 0 for flere alternativer) \n'.format(fjellvalg)))

    else:
        for i in valg:
            print(teller,'-',i.text)
            teller+=1
        bruker=int(input('Du søkte "{}", hvilken tur tenker du på?\n'.format(fjellvalg)))

    if bruker == 0:
        for i in valg[5:len(valg)]:
            print(teller,'-',i.text)
            teller+=1
            if teller >=10:
                      break
        bruker=int(input('Du søkte "{}", hvilken tur tenker du på? \n'.format(fjellvalg)))
    
    valg=valg[(bruker)-1]
    valg.click()
    resultat=browser.current_url
    hentinfo(resultat,fjellvalg)

def hentinfo(nettside,fjell):
    kilde = requests.get(nettside)
    soup = BeautifulSoup(kilde.content, 'html.parser')
    info = soup.find(class_='Container-text')
    turinfo = browser.find_element_by_class_name('info-list')
    turinfo = turinfo.text.split('\n')
    teller=0
    print('Her er informasjon om turen til {}:'.format(fjell),'\n')
    for i in range(6):
        print(turinfo[teller],'-',turinfo[teller+1])
        teller=teller+2

finnfjell()
