from selenium import webdriver
import threading
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from datetime import datetime


def test_logic():


    driver = webdriver.Chrome(executable_path=r'./chromedriver')
    url = 'https://discordapp.com/channels/'
    driver.get(url)

    t = threading.current_thread()
    print(datetime.now(), t.name, 'Discord Launched, Searching For Fields.')
    inputElement = driver.find_element_by_xpath("//*[@type='email']")
    inputElement.send_keys('arguetaoswaldo@yahoo.com')
    print(datetime.now(), t.name,'Typing in email bar')

    inputElement = driver.find_element_by_xpath("//*[@type='password']")
    inputElement.send_keys('playa0976')
    print(datetime.now(), t.name,'Typing in password bar')


    # Implement your test logic
    time.sleep(20)
    driver.quit()

def multi():

    N = 5   # Number of browsers to spawn
    thread_list = list()

    # Start test
    for i in range(N):
        t = threading.Thread(name='Task {}'.format(i), target=test_logic)
        t.start()
        #time.sleep(1)
        print (datetime.now(),t.name , 'started!')
        thread_list.append(t)

    # Wait for all thre<ads to complete
    for thread in thread_list:
        thread.join()

    print (datetime.now(), 'Test completed for %d tasks!' %N)


multi()
