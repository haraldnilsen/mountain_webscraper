from scraping import get_available_mountains, get_mountain_information
from selenium import webdriver
import os

# Functions
def find_mountain():
    browser = webdriver.Chrome(os.environ.get('DRIVER_LOCATION'))
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    user_mountain = input('Hvilket fjell skal du på? ')
    
    mountain_name = get_available_mountains(browser, user_mountain)

    get_mountain_information(browser, mountain_name)


# Main Execution
if __name__ == "__main__":
    # Main Function Call
    find_mountain()