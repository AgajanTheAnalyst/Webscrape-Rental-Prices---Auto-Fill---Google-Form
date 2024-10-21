import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Webscraping:
    def __init__(self, link):
        self.driver = webdriver.Chrome()
        self.response = requests.get(link)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        self.links = []
        self.prices = []
        self.addresses = []

    def webscrape(self):
        rental_property_data = self.soup.find_all('li', class_='ListItem-c11n-8-84-3-StyledListCardWrapper')
        for data in rental_property_data:
            address = ''.join(data.findNext('a', class_='StyledPropertyCardDataArea-anchor').get_text().split('\n'))
            fixed_address = ' '.join(address.split())
            self.addresses.append(fixed_address)
            price = str(data.findNext('span', class_='PropertyCardWrapper__StyledPriceLine').get_text())
            self.prices.append(price[:6])
            links = data.findNext('a', href=True)
            self.links.append(links['href'])
        print(self.links)
        print(self.prices)
        print(self.addresses)

    def fill_in(self, link):
        self.driver.get(link)
        data = [[self.addresses[i], self.prices[i], self.links[i]] for i in range(len(self.addresses))]
        for a in range(len(data)):
            fill_in = self.driver.find_elements(By.TAG_NAME, 'textarea')
            for b in range(len(fill_in)):
                fill_in[b].send_keys(data[a][b])
                time.sleep(1)
            time.sleep(3)
            WebDriverWait(self.driver, 3).until(
                ec.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'))

            ).click()
            WebDriverWait(self.driver, 3).until(
                ec.element_to_be_clickable((By.TAG_NAME, 'a'))
            ).click()
