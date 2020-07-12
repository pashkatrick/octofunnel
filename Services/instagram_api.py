import logging
from random import randint
from time import sleep

from selenium import webdriver

import config as conf


class Instagram(object):

    def __init__(self, username, password, token, headless=True):

        self.url = 'https://instagram.com/'
        self.selectors = {
            'username_field': 'username',
            'password_field': 'password',
            'button_login': 'button[type="submit"]',
            'search_user': 'queryBox',
            'select_user': 'span[aria-label="Выбрать / отменить выбор пользователя"]',
            'next_step': '//div[text()="Далее"]',
            'message_field': '*//textarea',
            'textarea': 'textarea',
            'send': '//button[text()="Отправить"]'
        }

        # Selenium config
        opts = webdriver.ChromeOptions()
        opts.add_argument("user-agent=PhantomJS")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        opts.add_experimental_option("prefs", prefs)
        opts.add_argument('user-data-dir=' + conf.get_sessions_path() + '/' + token)
        opts.binary_location = conf.get_chromium_path()
        if headless:
            opts.add_argument('headless')

        self.driver = webdriver.Chrome(conf.get_driver_path(), options=opts)

        try:
            self.login(username, password)
        except Exception as e:
            logging.error(e)

    def login(self, username, password):

        # login
        logging.info('Login with {}'.format(username))
        self.driver.get(self.url)
        self.__Sleep__(1)
        try:
            self.find_element_by_tag_name('img[data-testid="user-avatar"]')
        except:
            self.driver.find_element_by_name(self.selectors['username_field']).send_keys(username)
            self.driver.find_element_by_name(self.selectors['password_field']).send_keys(password)
            self.driver.find_element_by_tag_name(self.selectors['button_login']).click()
            self.__Sleep__(3)

    def sendMessage(self, user, message):
        logging.info('Send message {} to {}'.format(message, user))
        self.driver.get(self.url + 'direct/new/')
        self.driver.find_element_by_name(self.selectors['search_user']).send_keys(user)
        self.__Sleep__()

        # # Select user
        elements = self.driver.find_elements_by_tag_name(self.selectors['select_user'])
        elements[0].click()
        self.__Sleep__(1)

        # # Go to page
        self.driver.find_element_by_xpath(self.selectors['next_step']).click()
        self.__Sleep__()
        self.driver.find_elements_by_xpath(self.selectors['message_field'])[0].send_keys(message)
        self.__Sleep__(1)
        self.driver.find_element_by_xpath(self.selectors['send']).click()
        self.__Sleep__(1)

    def sendGroupMessage(self, users, message):
        logging.info('Send group message {} to {}'.format(message, str(users)))
        for user in users:
            self.sendMessage(user, message)

    def __randomSleep__(self, min=2, max=10):
        t = randint(min, max)
        logging.info('Wait {} seconds'.format(t))
        sleep(t)

    def __Sleep__(self, t=2):
        logging.info('Wait {} seconds'.format(t))
        sleep(t)

    def __scrolldown__(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
