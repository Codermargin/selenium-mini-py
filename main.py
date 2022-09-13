# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import errno

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
import logging
logging.getLogger().setLevel(logging.INFO)

class CustomChromeDriver:
    def __init__(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        # use relative chrome options
        options = ChromeOptions()
        # Open chrome || Start a session
        self.engine = webdriver.Chrome(service=service, options=options)
        logging.info(f'[Driver] Init Successfully')

    def goTo(self,url):
        self.engine.get(url)
        logging.info(f'[Driver] Browser go to {url}')

    def closeDriver(self):
        self.engine.quit()
        logging.info(f'[Driver] Quit Successfully')

    def delay(self,time):
        self.engine.implicitly_wait(time)
        logging.info(f'[Driver] Delay -> {time} secs')

    def click(self,element):
        logging.info(f'[Driver] Browser click {element}')
        button = self.engine.find_element(by=By.CSS_SELECTOR,value=element)
        button.click()

    def get_text(self,element):
        logging.info(f'[Driver] Browser get text from {element}')
        selector = self.engine.find_element(by=By.CSS_SELECTOR, value=element)
        return selector.text

    def input(self,element,text):
        logging.info(f'[Driver] Browser input {text} to {element}')
        selector = self.engine.find_element(by=By.CSS_SELECTOR, value=element)
        selector.send_keys(text)

    def clearInput(self,element):
        logging.info(f'[Driver] Browser clear {element} input')
        selector = self.engine.find_element(by=By.CSS_SELECTOR, value=element)
        selector.clear()

    def is_display(self,element):
        # TODO -> Can't handle retry in is display issue !!
        for i in range(5):
            if(self.engine.find_element(by=By.CSS_SELECTOR, value=element)):
                is_selector_visible = self.engine.find_element(by=By.CSS_SELECTOR, value=element).is_displayed()
                assert is_selector_visible == True
                logging.info(f'[Driver] Browser {element} is display')
                return
            self.delay(3)

def testRingCentral():
    try:
        driver = CustomChromeDriver()
        driver.goTo('https://app.ringcentral.com/')
        driver.click('*[data-test-automation-id="login-enter"]')
        driver.delay(10)
        driver.is_display('*[data-test-automation-id="loginCredentialNext"]')
        driver.input('*[data-test-automation-id="input"]', 'margin.test.test')
        driver.clearInput('*[data-test-automation-id="input"]')
        text = driver.get_text('*[data-test-automation-id="loginCredentialNext"]')
        assert text == 'Next'
        # driver.click('*[data-test-automation-id="loginCredentialNext"]')
    except Exception as e:
        print(e)
    else:
        driver.closeDriver()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testRingCentral()



