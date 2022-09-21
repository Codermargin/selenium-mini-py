from customChromeDriver import CustomChromeDriver


class FetchStockDriver:
    def __init__(self,url):
        self.driver = CustomChromeDriver()
        self.driver.goTo(url)

    def getName(self):
        stockNameArrElement = self.driver.get_all_elements('*[class="fundname"]')
        nameArr = []
        for element in stockNameArrElement:
            nameArr.append(element.text)
        return nameArr
    def getData(self):
        self.driver.get_all_elements()
