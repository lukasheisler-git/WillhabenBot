from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager



def main():
    #Credentials
    wh_name = ''
    wh_pass = ''

    # Initiate the browser
    browser  = webdriver.Chrome(ChromeDriverManager().install())

    #Enter Willhaben Page
    browser.get("https://www.willhaben.at/iad")
    browser.find_element_by_id( 'didomi-notice-agree-button').click()
    browser.get("https://www.willhaben.at/iad/myprofile/login?r=%2Fiad")

    #Fill credentials
    browser.find_element_by_id('email').send_keys(wh_name)
    browser.find_element_by_id('password').send_keys(wh_pass)
    browser.find_element_by_name('login').click()

    #Go to my adverts
    browser.get("https://www.willhaben.at/iad/anzeigenaufgabe?xtatc=INT-26")
    browser.find_element_by_id('newPrivateBap').click()

    #Create new add
    browser.find_element_by_id('ad_heading').send_keys('test objekt')
    browser.find_element_by_id('ad_price').send_keys('60')
    sleep(0.5)
    browser.find_element_by_id('showCategoryText').click()
    payload = 'Hier steht die beschreibung'
    browser.execute_script("tinyMCE.activeEditor.setContent('%s')" % payload)
    select = Select(browser.find_element_by_class_name("category-select"))
    sleep(0.5)
    select.select_by_value("4390")
    sleep(0.5)
    select = Select(browser.find_element_by_xpath("//select[@index = '1']"))
    select.select_by_value("4478")
    sleep(0.5)
    select = Select(browser.find_element_by_xpath("//select[@index = '2']"))
    select.select_by_value("4501")
    sleep(0.5)
    select = Select(browser.find_element_by_xpath("//select[@index = '3']"))
    select.select_by_value("4508")
    browser.find_element_by_id('saveAndContinueId').click()

    #Upload Images
    fu = browser.find_element_by_id("fileupload")


    fu.send_keys("/home/lukas/Documents/TheNetworkProject/WillhabenBot/Ads/test/1.png \n /home/lukas/Documents/TheNetworkProject/WillhabenBot/Ads/test/2.png")
    sleep(3)
    #fu.send_keys("/home/lukas/Documents/TheNetworkProject/WillhabenBot/Ads/test/2.png")
    #sleep(3)
    browser.find_element_by_id('saveAndContinueId').click()
    sleep(0.5)
    browser.find_element_by_id('saveAndContinueId').click()
    sleep(0.5)
    browser.find_element_by_id('saveAndContinueId').click()
    sleep(0.5)
    browser.find_element_by_name('_eventId_payAndPublish').click()

    input()


if __name__ == '__main__':
    main()
