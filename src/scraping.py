from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from bs4 import BeautifulSoup
import requests

def get_available_mountains(browser:webdriver.Chrome, user_mountain:str) -> str:
    """Searches for available mountains based on the given mountain name and
    displays them. Takes user input to further refine search results.

    @param browser: The Selenium WebDriver object used for web navigation.
    @type browser: selenium.webdriver.Chrome
    @param user_mountain: The name of the mountain to search for.
    @type user_mountain: str
        
    @rtype: None
    """
    browser.get('https://ut.no/')
    sleep(0.3)
    search=browser.find_element_by_id('input-field')
    search.send_keys(user_mountain)
    search.send_keys(Keys.ENTER)
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

    return resultat

def get_mountain_information(browser: webdriver.Chrome, mountain_name:str):
    """Searches for available mountains based on the given mountain name and
    displays them. Takes user input to further refine search results.

    @param browser: The Selenium WebDriver object used for web navigation.
    @type browser: selenium.webdriver.Chrome
    @param website_url: The url of the webpage containing information about the mountain.
    @type website_url: str
    @param mountain_name: The name of the mountain to search for.
    @type mountain_name: str
        
    @rtype: None
    """

    turinfo = browser.find_element_by_class_name('info-list')
    turinfo = turinfo.text.split('\n')
    teller=0
    print('Her er informasjon om turen til {}:'.format(mountain_name),'\n')
    for i in range(6):
        print(turinfo[teller],'-',turinfo[teller+1])
        teller=teller+2