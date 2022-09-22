from customChromeDriver import CustomChromeDriver


class XMUExtractor:
    def __init__(self,url):
        self.driver = CustomChromeDriver()
        self.driver.goTo(url)

    def getTutorInfo(self):
        tutorNameElements = self.driver.get_all_elements('*[class="col-md-4 col-sm-6 col-xs-12 pic-item"] *[class="text-primary"]')
        introElements = self.driver.get_all_elements('*[class="col-md-4 col-sm-6 col-xs-12 pic-item"] *[class="zc"]')
        directionElements = self.driver.get_all_elements('*[class="col-md-4 col-sm-6 col-xs-12 pic-item"] *[class="sz-info clearfix"]')
        dataDic = {}
        for i in range(len(tutorNameElements)):
            dataDic[tutorNameElements[i].text] = {
                'intro':introElements[i].text,
                'direction': directionElements[i].text
            }
        return dataDic

    def getIntro(self):
        self.driver.get_all_elements()
