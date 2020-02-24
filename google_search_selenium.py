from selenium import webdriver

class google():
    def __init__(self):
        self.driver=webdriver.Chrome()
        
    def search_en_google(self,sentence):
        self.driver.get("https://google.es")
        search=self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.send_keys(sentence)
        search_buttom=self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
        search_buttom.click()
    
    def search_google_images(self,sentence):
        self.driver.get("https://www.google.es/imghp?hl=es&tab=wi&ogbl")
        search=self.driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
        search.send_keys(sentence)
        search_buttom=self.driver.find_element_by_xpath('//*[@id="sbtc"]/button')
        search_buttom.click()
    def load_all_images(self):
        for i in range(3000):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
        try:
            buttom = self.driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input')
            buttom.click()
        except:
            print("no button")
            
        for i in range(3000):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    def get_images(self):
        return self.driver.find_elements_by_tag_name('img')