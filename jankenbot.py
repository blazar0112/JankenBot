import random
import schedule
import time
from datetime import datetime
from enum import Enum
from selenium import webdriver

url = 'https://p.eagate.573.jp/game/bemani/bjm2020/janken/index.html'

# change path to where you put chromedriver.exe
chrome_driver_path = R'D:\install\chromedriver_win32\chromedriver.exe'

class Strategy(Enum):
    Fixed = 0
    Random = 1

class Move(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

# you can change strategy to Strategy.Fixed or Strategy.Random
strategy = Strategy.Random
# you can change fixed move, only used when strategy is Strategy.Fixed
fixed_move = Move.Scissors

# =================================================================
# Don't modify anything below
# =================================================================

japanese_names = { Move.Rock:'グー', Move.Paper:'パー', Move.Scissors:'チョキ' }

driver = webdriver.Chrome(executable_path=chrome_driver_path)
print('janken page url:'+url)

def print_stamp():
    try:
        stamp_element = driver.find_element_by_xpath('//*[@id="inc-janken"]/div/div/p[2]/strong')
        print('Current stamp =', stamp_element.text+'.')
    except:
        print('Cannot find stamp count.')

def check_janken_page():
    print(datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'), "Checking janken page...")
    driver.get(url)
    try:
        error_element = driver.find_element_by_xpath('//*[@id="error"]')
        print('Login error, manually login!')
        foo = input('Type anything after login to continue: ')
    except:
        pass

    try:
        move = fixed_move
        if strategy==Strategy.Random:
            move = random.choice(list(Move))
        select_element = driver.find_element_by_xpath('//*[@id="janken-select"]/div/a['+str(move.value)+']')
    except:
        print('Already selected move.')
        print_stamp()
        return

    select_url = select_element.get_attribute('href')
    print('select_url: ', select_element.get_attribute('href'))
    driver.get(select_url)
    print('Move selected as', move.name, '[JP:', japanese_names[move]+']')
    driver.get(url)
    print_stamp()

schedule.every().hour.do(check_janken_page)

check_janken_page()

while True:
    schedule.run_pending()
    time.sleep(1)