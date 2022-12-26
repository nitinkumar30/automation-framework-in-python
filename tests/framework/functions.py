# from selenium.webdriver.common.keys import Keys
import os

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


# chromedriver
def chromedriver_initiator():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--start-maximized")
    chromedriver_autoinstaller.install()
    return webdriver.Chrome(options=opt)


# wait
def wait(secs):
    time.sleep(secs)


# click element
def clickBy_Xpath(browser, xpath):
    wait(3)
    return browser.find_element(By.XPATH, xpath).click()


# send keys
def sendKeys_Xpath(browser, text, xpath):
    wait(3)
    browser.find_element(By.XPATH, xpath).clear()
    browser.find_element(By.XPATH, xpath).send_keys(text)


# check text
def extractText(browser, xpath):
    wait(3)
    return browser.find_element(By.XPATH, xpath).text


def extractText_multiple(browser, xpath):
    wait(3)
    res = []
    s = browser.find_elements(By.XPATH, xpath)
    for i in s:
        res.append(i.text)
    return res


# select option from dropdown
def optionfromDrop_text(browser, xpath, text):
    wait(3)
    sel = Select(browser.find_element(By.XPATH, xpath))
    sel.select_by_visible_text(text)


# Clicks a button on every iteration
def clickBtn_multiple(browser, xpath):
    wait(3)
    res = []
    xp = []
    s = browser.find_elements(By.XPATH, xpath)
    print(s)

    for i in s:
        if i.is_displayed():
            res.append(i.text)
            a = clickBy_Xpath(browser, xpath)
            xp.append(a)
    return res, xp


# Empty a directory
def emptyDirectory(browser, directoryName):
    # lstOfFiles = os.listdir(directoryName)
    for i in os.listdir(directoryName):
        fullPath = directoryName + i
        os.remove(fullPath)


# Take screenshot
def screenshot(browser, filename):
    browser.save_screenshot('./evidences/'+filename+'.PNG')

# upload file

