from selenium import webdriver
from userInfo import username, password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Instagram:
    driver_path = "C:/Users/yaree/Drivers/chromedriver.exe"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(Instagram.driver_path)
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element(By.NAME, "username")
        passwordInput = self.browser.find_element(By.NAME, "password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        passwordInput.send_keys(Keys.ENTER)

        time.sleep(4)
        
        if(self.browser.find_element(By.CLASS_NAME, 'cmbtv')):
            el = self.browser.find_element(By.CLASS_NAME, 'cmbtv')
            el.find_element(By.TAG_NAME,'button').click()

        time.sleep(4)

        if(self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')):
            self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()

    def followUser(self,username):
        self.browser.get(f"https://www.instagram.com/{username}") 
        time.sleep(3)

        if(self.browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button')):
            followButton = self.browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button')
    
        if followButton.text == "Follow":
            followButton.click()
            time.sleep(2)
        else:
            print(f"{username} sayfasını zaten takip ediyorsunuz...")

    def followUsers(self, users):
        for user in users:
            self.followUser(user)

   
    def __del__(self):
        time.sleep(10)
        #self.browser.close()



app = Instagram(username, password)

app.signIn()
app.followUsers(["kod_evreni","yazilimatolyesi"])
