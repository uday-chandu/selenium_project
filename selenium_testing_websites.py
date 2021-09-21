from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.common.exceptions import ElementNotVisibleException,TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time,requests
import os
import os.path
import warnings
warnings.filterwarnings('ignore')
class pixabay_website():
    def __init__(self,search_keyword,number):
        self.search_keyword=search_keyword
        self.number=int(number)
    def img_download(self):
        try:
            browser=Chrome(ChromeDriverManager().install())
            browser.maximize_window()
            #googling the site
            browser.get('https://pixabay.com/')
            try:
                #browser check
                WebDriverWait(browser, 30, 1, (ElementNotVisibleException,TimeoutException)).until(lambda x: x.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div/div[1]").is_displayed())#clicks on pixaby image to make sure that the user at main page
                browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div/div/div[1]').click()
            except:
                pass
            #wait until the login button appears
            attempt=1
            while(attempt):
                try:
                    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/ul/li[2]').click()
                    break
                except:
                    attempt+=1
            #click on login button
            browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/ul/li[2]').click()
            time.sleep(5)
            #inserts username and password and clicks on login or submit
            browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div[1]/div/div[1]/form/p[1]/input').send_keys('udaychowdary503@gmail.com')
            browser.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/div[2]/div[1]/div/div[1]/form/p[2]/input').send_keys('ammananna503@Uday')
            browser.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/div[1]/div/div[1]/form/div/input").click()
            #time to press on captcha
            img_present=WebDriverWait(browser, 30, 1, (ElementNotVisibleException,TimeoutException)).until(lambda x: x.find_element_by_xpath("/html/body/div[1]/div[1]/div/a").is_displayed())#clicks on pixaby image to make sure that the user at main page
            #clicks on pixaby image to make sure that the user at main page
            attempt=1
            while(attempt):
                try:
                    if img_present==True:
                        browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/a').click()
                    else:
                        browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/a').click()
                    break
                except:
                    attempt+=1
            #input to give by user to search for desired images
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[4]/form/div/span/input").clear()
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[4]/form/div/span/input").send_keys(self.search_keyword,Keys.ENTER)
            #creating a folder
            if os.path.isdir('selenium_pixabay'):
                print('folder is present')
            else:
                os.mkdir('selenium_pixabay')
                print('folder is absent, so created!')

            if os.path.isdir('selenium_pixabay/website_images'):
                print(" folder exists, so the download images are gonna stored")
            else:
                os.mkdir('selenium_pixabay/website_images')
                print("folder doesn't exists,so a folder created")
            #storing the image name into a list inorder to name them as a file name
            website_images=[]
            img_no=1
            for i in range(1,self.number+1):
                img_name=browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div/div[3]/div["+str(i)+"]").text
                img_name=self.search_keyword+'_img'+str(img_no)
                src=browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[3]/div/div[3]/div["+str(i)+"]/div/div/div/a/img").get_attribute('src')
                r = requests.get(src,verify=False,stream=True)
                with open("selenium_pixabay/website_images/"+img_name+".png","wb") as fd:
                    for chunk in r.iter_content(chunk_size=20480*20480):
                        fd.write(chunk)
                        fd.flush()
                img_no+=1
            print('images got downloaded, check the folder')
            browser.quit()
        except Exception as e:
            print(e.args)
            browser.quit()