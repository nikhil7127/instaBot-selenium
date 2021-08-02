from selenium import webdriver
import time as t 
from selenium.webdriver.common.keys import Keys

class bot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\selenium_python\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
    
    def home(self):
        self.driver.find_element_by_class_name('s4Iyt').click()
            
    def remove(self):
        self.driver.implicitly_wait(10)
        t.sleep(2)
        self.driver.find_element_by_xpath(r'//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_class_name('HoLwm').click()
   
    def login(self,userName,Password,show = False):
        self.driver.implicitly_wait(10)
        values = self.driver.find_elements_by_class_name("_2hvTZ")
        values[0].send_keys(userName)
        t.sleep(2)
        values[1].send_keys(Password)
        self.driver.implicitly_wait(10)
        t.sleep(2)
        show and self.driver.find_element_by_class_name('_8A5w5').click()
        show and t.sleep(2)
        self.driver.find_element_by_class_name('L3NKy').click()
        try:
            self.remove()
        except:
            pass
    
    def message(self, Name,message):
        self.home()
        if (type(message) == str or len(Name) == len(message)):
            self.driver.find_element_by_class_name('xWeGp').click()
            self.driver.implicitly_wait(10)
            for index,name in enumerate(Name):
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
                self.driver.implicitly_wait(10)
                t.sleep(2)
                self.driver.find_element_by_class_name('j_2Hd').send_keys(name)
                self.driver.implicitly_wait(5)
                t.sleep(2)
                self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]').click()
                self.driver.implicitly_wait(5)
                t.sleep(2)
                self.driver.find_element_by_class_name('cB_4K').click()
                self.driver.implicitly_wait(5)
                t.sleep(2)
                type(message) == str and self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message,Keys.ENTER)
                not type(message) == str and self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message[index],Keys.ENTER)
                print("message send to "+ name)
        else:
            print("Enter valid input")
   
    def follow(self,Names):
        self.home()
        for name in Names:
            self.driver.find_element_by_class_name("x3qfX").send_keys(name)
            self.driver.implicitly_wait(5)
            t.sleep(2)
            self.driver.find_element_by_class_name("-qQT3").click()
            t.sleep(2)
            self.driver.implicitly_wait(5)
            isValid = self.driver.find_elements_by_class_name("-fzfL")
            if(not isValid):
                let = self.driver.find_element_by_class_name("BY3EC").find_elements_by_class_name("sqdOP")
                if(let):
                    self.driver.find_element_by_class_name("BY3EC").find_element_by_class_name('L3NKy').click()
                else:
                    self.driver.find_element_by_class_name("jIbKX").click()
                print("Sucessfully Followed : "+ name)
                t.sleep(1)
            else:
                print("Already Following : " + name)


    def unfollow(self,Names):
        self.home()
        for name in Names:
            self.driver.find_element_by_class_name("x3qfX").send_keys(name)
            self.driver.implicitly_wait(5)
            t.sleep(2)
            self.driver.find_element_by_class_name("-qQT3").click()
            t.sleep(2)
            self.driver.implicitly_wait(5)
            isValid = self.driver.find_elements_by_class_name("-fzfL")
            if(isValid):
                isValid[0].click()
                t.sleep(2)
                self.driver.find_elements_by_class_name("aOOlW")[0].click()
                print("Sucessfully unFollowed: "+ name)
            else:
                print("Not Following")
            t.sleep(2)

    def scroll(self,item):
        a,b = 0,1
        while(a!=b):
            a = b
            t.sleep(2)
            self.driver.implicitly_wait(10)
            self.driver.execute_script("arguments[0].scrollTo(0,arguments[0].scrollHeight)",item)
            b = self.driver.execute_script("return arguments[0].scrollHeight",item)    

    def GetDetails(self,index,individual=True):
        listOf = []
        if(individual):
            self.home()
            self.driver.implicitly_wait(10)
            t.sleep(5)
            self.driver.find_elements_by_class_name("Fifk5")[-1].click()
            self.driver.implicitly_wait(10)
            t.sleep(2)
            self.driver.find_element_by_class_name("-qQT3").click()
            t.sleep(2)
        gets = self.driver.find_elements_by_class_name("-nal3")
        self.driver.implicitly_wait(10)
        gets[index].click()
        self.driver.implicitly_wait(10)
        t.sleep(2)
        self.scroll(self.driver.find_element_by_class_name("isgrP"))
        t.sleep(3)
        for k in self.driver.find_elements_by_class_name("MqpiF"):
            listOf.append(k.text)
        t.sleep(2)
        self.driver.find_elements_by_class_name("wpO6b")[-1].click()
        return listOf
    
    def followers(self,saveas ="followers"):
        return self.GetDetails(1)

    def following(self,saveas="following"):
        return self.GetDetails(-1,False)

    def compare(self,me=False):
        followers = self.followers()
        following = self.following()
        notfollowing =[]
        if(me):
            for f1 in followers:
                if f1 in following:
                    pass
                else:
                    notfollowing.append(f1)
            return notfollowing

        else:
            for f1 in following:
                if f1 in followers:
                    pass
                else:
                    notfollowing.append(f1)
            return notfollowing

if __name__ == "__main__":
    try:
        bots = bot()
    except:
        print("Check Your Internet Connection")

    bots.login("userName","Password")
    print(bots.compare(me=True))
    bots.message(userNameList)
    bots.unfollow(userNamesList)
    bots.follow(userNamesList)

    t.sleep(10)
