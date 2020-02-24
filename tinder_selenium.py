from selenium import webdriver
#https://github.com/aj-4/tinder-swipe-bot/blob/master/tinder_bot.py
class TinderBot():
    def __init__(self):
        self.driver=webdriver.Chrome()
        
    def login(self,user,password):
        self.driver.get("https://tinder.com")
        time.sleep(5)
        #click login buttom
        fb_login=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_login.click()
        #move to pop up window
        self.base_window=self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        
        #login in facebook
        email_in=self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(user)
        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)
        fb_logint_entrar=self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        fb_logint_entrar.click()
        
        #move to base window
        self.driver.switch_to_window(self.base_window)
        
        #permision
        time.sleep(2)
        allow_location_buttom=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        allow_location_buttom.click()
        time.sleep(2)
        use_tinder_buttom=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        use_tinder_buttom.click()
        time.sleep(2)
        hallow_tinder_notifications_buttom=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        hallow_tinder_notifications_buttom.click()
        
    def like1(self): 
        like_buttom = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_buttom.click()
        
    def like2(self):
        like_buttom=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[3]')
        like_buttom.click()
        
    def dislike1(self):
        dislike_buttom = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_buttom.click()
        
    def dislike2(self):
        dislike_buttom=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[1]')
        dislike_buttom.click()
    
    def get_name(self):
        name_id=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div/span')
        return name_id.text
    def get_age(self):
        age_id=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/span')
        return age_id.text
    
    def get_screenshot(self):
        name=self.get_name()
        self.driver.save_screenshot(name+'_'+self.driver.session_id+'.png')
    
    def like(self):
        self.get_screenshot()
        self.like1()