from XMU.XMUExtractor import XMUExtractor
from fetchStockDriver import FetchStockDriver

def test():
    try:
        XMN_COMPUTER_URL = 'https://informatics.xmu.edu.cn/szdw/jcrc.htm'
        a=[]
        extractor = XMUExtractor(XMN_COMPUTER_URL)
        res = extractor.getTutorInfo()
        print(f'厦大信息学院数据 -> {res}')
        # stockUrl = 'https://m.1234567.com.cn/index.html?page=jjph&tab=qb'
        # driver = FetchStockDriver(stockUrl)
        # fundNamesArr = driver.getName()
        # print(f'基金排名表数据 -> {fundNamesArr}')
        # driver = CustomChromeDriver()
        # driver.goTo('https://app.ringcentral.com/')
        # driver.click('*[data-test-automation-id="login-enter"]')
        # driver.delay(10)
        # driver.is_display('*[data-test-automation-id="loginCredentialNext"]')
        # driver.input('*[data-test-automation-id="input"]', 'margin.test.test')
        # driver.clearInput('*[data-test-automation-id="input"]')
        # text = driver.get_text('*[data-test-automation-id="loginCredentialNext"]')
        # assert text == 'Next'
        # driver.click('*[data-test-automation-id="loginCredentialNext"]')
    except Exception as e:
        print(e)
    else:
        driver.closeDriver()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()



