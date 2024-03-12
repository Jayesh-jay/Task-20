from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests


class DownloadMonthlyProgressReport:
    def __init__(self, url="https://labour.gov.in/"):
        self.url = url
        self.driver = webdriver.Chrome()

    def __boot__(self):
        self.driver.get(self.url)
        sleep(3)
        self.driver.maximize_window()
        sleep(2)

    def quit(self):
        sleep(3)
        self.driver.quit()

    def getelementbyXPATH(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def closepopupbody(self):
        self.getelementbyXPATH('//*[@id="popup"]/div[2]/button').click()
        print("Success: The popup closed")
        sleep(5)

    def downlooadprogressreport(self):
        documentelement = self.getelementbyXPATH('//*[@id="nav"]/li[7]/a')
        ActionChains(self.driver).move_to_element(documentelement).perform()
        self.getelementbyXPATH('//*[@id="nav"]/li[7]/ul/li[2]/a').click()
        print("Success: Clicked on the monthly progress report")
        sleep(3)

    def opendocument(self):
        self.getelementbyXPATH(
            '//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').click()
        self.driver.switch_to.alert.accept()
        print("Success: The document opened")

    def downloaddocument(self):
        url = self.driver.current_url
        print("the url of the document is", url)
        response = requests.get(url)
        if response.status_code == 200:
            filepath = "monthlyprogressreport.pdf"
            with open(filepath, "wb") as f:
                f.write(response.content)
            print("Success: Document downloaded")
        else:
            print("Error")


if __name__ == "labour_document":
    obj = DownloadMonthlyProgressReport()
    obj.__boot__()
    obj.closepopupbody()
    obj.downlooadprogressreport()
    obj.opendocument()
    obj.downloaddocument()

