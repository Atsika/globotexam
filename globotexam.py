from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from time import sleep




art = '''  _____ _       _           _   ______
  / ____| |     | |         | | |  ____|
 | |  __| | ___ | |__   ___ | |_| |__  __  ____ _ _ __ ___
 | | |_ | |/ _ \| '_ \ / _ \| __|  __| \ \/ / _` | '_ ` _  \\
 | |__| | | (_) | |_) | (_) | |_| |____ >  < (_| | | | | | |
  \_____|_|\___/|_.__/ \___/ \__|______/_/\_\__,_|_| |_| |_|



            Made with ♥ by Astika & léco.'''
print(art)
sleep(3)



username = input("Entrez votre username : ")
password = getpass("Entrez votre password : ")
url = "https://business.global-exam.com/login"
driver = webdriver.Firefox()

driver.get(url)
sleep(10)
driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("password").send_keys(password, Keys.ENTER)
sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div").click()
sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/div").click()
# partie 5
sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div/h4").click()
sleep(5)
for i in range(1, 26):
    sleep(5)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[" + str(i) + "]/div/div[2]").click()
    sleep(5)
    driver.find_element_by_id("start_session").click()
    sleep(5)
    for k in range(1, 7):
        for j in range(1,6):
            q = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div[2]/form/div[1]/div[" +str(j) + "]")
            sleep(3)
            show = driver.find_elements_by_xpath("//*[@id='toggle_guidelines']")
            sleep(3)
            show[j-1].click()
            sleep(3)
            val = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div[2]/form/div[1]/div[" + str(j) + "]/div[4]/div/div/div/ul[1]/li/div/input").get_attribute("value")
            sleep(3)
            q.find_element_by_xpath("//input[@value='" + str(val) + "']/following-sibling::label").click()
            sleep(5)
        try:
            sleep(5)
            driver.find_element_by_id("next_part").click()
            sleep(3)
        except:
            sleep(1300)
            driver.find_element_by_id("finish_session").click()
            sleep(3)

    sleep(5)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/button[1]").click()
    sleep(5)
