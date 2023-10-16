# Mountain Info Web Scraper

## Description
This Python script allows you to enter the name of a mountain and retrieve information about that mountain. The script uses Selenium for web automation and BeautifulSoup for HTML parsing to scrape data from `https://ut.no/`. The project was made as my first python-project back in 2019 to learn webscraping, but the code has later been refactored.

#### Contribution/further development
The project is pretty barebones right now and is mostly used for learning webscraping, but for anyone that wants to submit PR's, this i what i want to add to the project:
- A frontend application.
- Connecting the application to a Google Maps API to be able to estimate how long time a total trip will take.
- Endpoints to make it a fully functional API.

#### Using the program in the CLI
![Showing the app](./img/image.png)

## Prerequisites
- Python 3.x
- Selenium
- BeautifulSoup
- requests
- Chrome WebDriver

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/haraldnilsen/UT.no_webscraper.git
    ```
    
2. Navigate to the project directory:
    ```
    cd mountain_webscraper
    ```
    
3. Install required Python packages:
    ```
    pip install -r requirements.txt
    ```
    
4. Download [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/), find a location and update the environment variable.

## Usage

Run the script by executing: 
```bash
    python3 src/main.py
    ```
    