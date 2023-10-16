from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
    sleep(0.5)

    if (browser.find_element(By.CLASS_NAME, 'coi-button-group') != None):
        sleep(0.5)
        accept_cookie_button = browser.find_element(By.CLASS_NAME, 'coi-banner__accept')
        accept_cookie_button.click()
        sleep(0.5)

    search = browser.find_element(By.ID, 'input-field')
    search.send_keys(user_mountain)
    search.send_keys(Keys.ENTER)
    sleep(0.5)
    
    categories=browser.find_elements(By.CLASS_NAME, 'explore-page-search__category')
    correct_category = categories[2]
    options = correct_category.find_elements(By.CLASS_NAME, 'explore-page-search__item-link')

    teller=1
    if len(options)>5:
        for i in options[:5]:
            print(teller,'-',i.text)
            teller+=1
        bruker=int(input('Du søkte "{}", hvilken tur tenker du på? (skriv 0 for flere alternativer) \n'.format(user_mountain)))

    else:
        for i in options:
            print(teller,'-',i.text)
            teller+=1
        bruker=int(input('Du søkte "{}", hvilken tur tenker du på?\n'.format(user_mountain)))

    if bruker == 0:
        for i in options[5:len(options)]:
            print(teller,'-',i.text)
            teller+=1
            if teller >=10:
                      break
        bruker=int(input('Du søkte "{}", hvilken tur tenker du på? \n'.format(user_mountain)))

    options=options[bruker-1]
    options.click()
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
    sleep(0.5)
    turinfo = browser.find_element(By.CLASS_NAME, 'info-list')
    turinfo = turinfo.text.split('\n')
    print('Her er informasjon om turen til {}:'.format(mountain_name),'\n')
    for i in range(0, len(turinfo) - 1):
         print(turinfo[i])