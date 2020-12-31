from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time




def SendMessage( message , targets , toSendImage , caption , toSendDocuement , imagepath , documentpath  ):


    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://web.whatsapp.com/")

    def waiting():
        while True:
                try:
                    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@data-icon="msg-time"]')))
                except TimeoutException:
                    break   



    wait = WebDriverWait(driver, 20)
    wait5 = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/div")))
    #search for contacts
    for target in targets:

        try :
            target = int(target)
            target = str(target)
            waiting()  
            
            if(len(target) == 10 ):
                target = "91" + target
            
            
            driver.get("https://web.whatsapp.com/send?phone="+target+"&text&app_absent=1")
            '''alert = driver.switch_to_alert()
            alert.accept()'''
            #time.sleep(2)
            #waiting until the message button is visible
            # try:
            #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="action-button"]')))
            #     time.sleep(2)
            #     driver.find_element_by_xpath('//*[@id="action-button"]').click()
            # except TimeoutException:
            #     print("Timeout")
            #     driver.find_element_by_xpath('//*[@id="action-button"]').click()
            
            try:
                
                #finding if number is not valid
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[text()='Phone number shared via url is invalid.']")))
                #driver.find_element_by_xpath("//*[text()='Phone number shared via url is invalid.']")
                #time.sleep(5)
                ok_path = "/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div"

                driver.find_element_by_xpath(ok_path).click()
                print("Invalid number: "+target+"\n")
                time.sleep(2)

                #if number not valid then continue with next number
                continue
            except TimeoutException:
                #print("Valid number: "+target)
                pass
    

        except ValueError: 
            #print(target + " is a string")
            

            x_arg = '//span[contains(@title,' + target + ')]'
            time.sleep(2)
            try:
                wait5.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                #search the element

            except:
                # If the name of contact is not found then search for the contact
                # click the search button
                inputSearchBox = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input')
                time.sleep(1)
                inputSearchBox.clear()
                inputSearchBox.send_keys(target[1:len(target) - 1])
                print('Target Searched')
                time.sleep(1)

            # Select the contact
            driver.find_element_by_xpath(x_arg).click()
            time.sleep(2)

        # Select the chat box 
        time.sleep(2)
        inp_xpath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
        time.sleep(2)

        #Sending Message

        for ch in message:
            if ch == "\n":
                ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)

        input_box.send_keys(Keys.ENTER)
        #if image is selected
        if (toSendImage==1):
            import autoit
            clipButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
            clipButton.click()
            time.sleep(1)

            # To send Videos and Images.
            mediaButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span')
            
            mediaButton.click()
            time.sleep(3)
            autoit.control_focus("Open","Edit1")
            autoit.control_set_text("Open","Edit1",(imagepath) )
            autoit.control_click("Open","Button1")

            time.sleep(7)
            captionbox = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/span/div/div[2]/div/div[3]/div[1]/div[2]')
            for ch in caption:
                if ch == "\n":
                    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
                else:
                    captionbox.send_keys(ch)

            time.sleep(1)

            whatsapp_send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
            whatsapp_send_button.click()
            #image sent
        #to send document
        if(toSendDocuement==1):
            import autoit
            clipButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span')
            clipButton.click()
            time.sleep(1)

            docButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[3]/button/span')
            docButton.click()
            time.sleep(1)

            autoit.control_focus("Open","Edit1")
            autoit.control_set_text("Open","Edit1",(documentpath) )
            autoit.control_click("Open","Button1")

            time.sleep(3)
            whatsapp_send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
            whatsapp_send_button.click()

        print("Message sent to : "+ target + '\n')

    waiting()
    print("Messages sent to all numbers")
    driver.quit()
    