from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
form_link = "https://docs.google.com/forms/d/e/1FAIpQLSd4WguC3foHn-mG7bnsKmi9dJaOAPfoHBiLpcub5R5B6N_4iQ/viewform?usp=sf_link"
chrome_driver_path = "C:\Development\chromedriver.exe"

class Form():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def fill_form(self, prices, new_links, addresses):
        self.driver.get(form_link)
        time.sleep(2)
        price = self.driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address = self.driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        price.send_keys(prices)
        address.send_keys(addresses)
        link.send_keys(new_links)
        time.sleep(2)
        button.click()