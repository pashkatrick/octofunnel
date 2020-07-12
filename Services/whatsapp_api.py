import logging
from random import randint
from time import sleep

from selenium import webdriver

import config as conf


class Whatsapp(object):

    def __init__(self, token, headless=False):
        self.url = 'https://web.whatsapp.com/'
        self.selectors = {
            'select_contact': 'div[role="option"]',
            'input_field': 'div.selectable-text',
            'send': 'span[data-testid="send"]'
        }
        # Selenium config
        opts = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        opts.add_experimental_option("prefs", prefs)
        opts.add_argument('user-data-dir=' + conf.get_sessions_path() + '/' + token)
        opts.binary_location = conf.get_chromium_path()
        if headless:
            opts.add_argument('headless')
        self.driver = webdriver.Chrome(conf.get_driver_path(), options=opts)

    def sendMessage(self, phone, message):
        logging.info('Send message {} to {}'.format(message, phone))
        self.driver.get(self.url + 'send?phone=7' + phone)
        self.__Sleep__(4)
        self.driver.find_elements_by_css_selector(self.selectors['input_field'])[1].send_keys(message)
        self.driver.find_element_by_tag_name(self.selectors['send']).click()
        self.__Sleep__(2)

    def sendGroupMessage(self, phones, message):
        logging.info('Send group message {} to {}'.format(message, str(phones)))
        for contact in phones:
            self.sendMessage(contact, message)

    def __randomSleep__(self, min=2, max=10):
        t = randint(min, max)
        logging.info('Wait {} seconds'.format(t))
        sleep(t)

    def __Sleep__(self, t=2):
        logging.info('Wait {} seconds'.format(t))
        sleep(t)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
