from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests


class DowloadImages:
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

    def ClickOnPhotoGallery(self):
        Mediaelement = self.getelementbyXPATH('//*[@id="nav"]/li[10]/a')
        ActionChains(self.driver).move_to_element(Mediaelement).perform()
        self.getelementbyXPATH('//*[@id="nav"]/li[10]/ul/li[2]/a').click()
        print("Success: Clicked on photo gallery")
        sleep(3)


    def downloaPhotos(self):
        sleep(2)
        for i in range(1,11):
            xpath= f'//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[{i}]/td[1]/div[1]/div/img'
            url= self.getelementbyXPATH(xpath).get_attribute("src")

            print("the url of the image is",url)
            response = requests.get(url)
            if response.status_code == 200:
                filepath = f"images/image {i}.png"
                f=open(filepath, "wb")
                f.write(response.content)
                f.close()
                print(f"images{i} is dowloaded")
            else:
                print("Error")



if __name__ == "__labour_media__":
    obj = DowloadImages()
    obj.__boot__()
    obj.closepopupbody()
    obj.ClickOnPhotoGallery()
    obj.downloaPhotos()
    obj.quit()

