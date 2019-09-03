import threading
import time
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from datetime import datetime


class ChangeTheMarket():

    def __init__(self):
        self.driver = None

    def setupselenium(self):
        options = Options()
        #options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('ignore-certificate-errors')
        #options.add_argument('incognito')
        #options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=r'/Users/BigO/Documents/CODE/Supreme_Community/chromedriver')

    def cleanUpBrowser(self):
        print(datetime.now(),'Quitting Browser')
        self.driver.quit()

    def execute(self):
        self.setupselenium()

        self.cleanUpBrowser()

    def Multithreading(self):
        N = 2   # Number of browsers to spawn
        thread_list = list()

        # Start test
        for i in range(N):
            t = threading.Thread(name='Test {}'.format(i), target=test_logic)
            t.start()
            time.sleep(1)
            print (t.name , ' started!')
            thread_list.append(t)

        # Wait for all thre<ads to complete
        for thread in thread_list:
            thread.join()

        print ('Test completed!')


        def manipulation(self):
        json_data = "./Tasks.json"
        with open(json_data) as f:
            accounts = dict(json.loads(f.read()))
            for task_num, values in enumerate(accounts[key]['tasks']): # by using enumerate we are itterating through the json to find the index so we know how many tasks will be placed.
                print ("%d : %s" % (task_num, values))

                task = accounts[key]['tasks']
                print(task[5])


        def sort(catagorie):
            if(catagorie ==  "Jackets"):
                return ("https://www.supremenewyork.com/shop/all/jackets")
            elif(catagorie ==  "Shirts"):
                return("https://www.supremenewyork.com/shop/all/shirts")
            elif(catagorie ==  "Tops/Sweaters"):
                return ("https://www.supremenewyork.com/shop/all/tops_sweaters")
            elif(catagorie ==  "Sweatshirts"):
                return ("https://www.supremenewyork.com/shop/all/sweatshirts")
            elif(catagorie ==  "Pants"):
                return ("https://www.supremenewyork.com/shop/all/pants")
            elif(catagorie ==  "Shorts"):
                return ("https://www.supremenewyork.com/shop/all/shorts")
            elif(catagorie ==  "T-Shirts"):
                return ("https://www.supremenewyork.com/shop/all/t-shirts")
            elif(catagorie ==  "Hats"):
                return ("https://www.supremenewyork.com/shop/all/hats")
            elif(catagorie ==  "Bags"):
                return ("https://www.supremenewyork.com/shop/all/bags")
            elif(catagorie ==  "Accessories"):
                return ("https://www.supremenewyork.com/shop/all/accessories")
            elif(catagorie ==  "Skate"):
                return ("https://www.supremenewyork.com/shop/all/skate")

                # items = "T-Shirts"
                # sort(items)
