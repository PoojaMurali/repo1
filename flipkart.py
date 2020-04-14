from selenium import webdriver

url = "https://www.flipkart.com/"
driver = webdriver.Chrome("Chromedriver.exe")
driver.get(url)

inputUsername=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
inputUsername.send_keys('hpooja751@gmail.com')
inputPassword=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
inputPassword.send_keys('9080322912')
submitbutton=driver.find_element_by_css_selector('body > div.mCRfo9 > div > div > div > div > div.Km0IJL.col.col-3-5 > div > form > div._1avdGP > button > span')
submitbutton.click()
sleep(3)
foundvalue=driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[3]/div/div/div/div')
foundname=foundvalue.text
print(foundname)
driver.close()

