from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import re
import time

'''
This class serves as a Scraper to get games using selenium
NOTE: Fetching data is too damn slow
      TAKES OVER 30 SECS TO FETCH
'''

class EpicGamesServices:

    def __init__(self) -> None:

        self.URL = 'https://store.epicgames.com/en-US/'
    
    
    def get_free_games(self) -> list[str]:

        list_of_games = []

        # Creating driver and accessing page
        headless_browser = Options()
        headless_browser.add_argument('-headless')
        driver = webdriver.Firefox(
            options = headless_browser, 
            service = Service(GeckoDriverManager().install())
            )
        driver.get(self.URL)
        
        # Get results
        results = driver.find_elements(By.CLASS_NAME, 'css-hkjq8i')
        for result in results:
            if re.search(r'\bFree Now\b', result.text):
                list_of_games.append(result.text + '\n')
        # Stop Driver
        driver.quit()

        for game in list_of_games:
            print(game)


if __name__ == '__main__':
    Bot = EpicGamesServices()
    start = time.time()
    Bot.get_free_games()
    end = time.time()
    print(f'Execution time: {end - start} \n')