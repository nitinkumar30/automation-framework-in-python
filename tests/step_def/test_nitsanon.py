from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.framework.functions import *
from tests.framework.variables import *
from tests.framework.xpaths import *

# Scenarios

scenarios('../features/nitsanon.feature')


# Fixtures

@pytest.fixture
def browser():
    # b = webdriver.Firefox()
    opt = webdriver.ChromeOptions()
    opt.add_argument("--start-maximized")
    chromedriver_autoinstaller.install()
    b = webdriver.Chrome(options=opt)
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps

@given('the nitsanon home page is displayed')
def ddg_home(browser):
    browser.get(nitsanonURL)
    print('\n\n\nOpen Browser >>> DEBUG')


@when('the user puts username and password')
def input_credentials(browser):
    browser.implicitly_wait(5)
    sendKeys_Xpath(browser, userValue, login_userInput)
    sendKeys_Xpath(browser, passValue, login_passInput)
    print('\n\n\n Credentials given >>> DEBUG')


@when('the user clicks on Sign In button')
def clicks_submit(browser):
    clickBy_Xpath(browser, login_submitBtn)
    print('\n\n\n Clicked >>> DEBUG')


@then('the user logs in successfully')
def logs_in(browser):
    links_div = browser.find_element(By.CLASS_NAME, "row")
    links_div.is_displayed()
    print('\n\n\n After logging In >>> DEBUG')


# -----------------------------------------

@when('the user clicks on signup button')
def clicks_signup(browser):
    clickBy_Xpath(browser, signup_Btn)
    print('\n\n\n Signup Button clicked >>> DEBUG')


@when('the user puts neccesary credentials for creating account')
def input_credentials(browser):
    sendKeys_Xpath(browser, signup_userValue, signup_userInput)
    sendKeys_Xpath(browser, signup_passValue, signup_passInput)
    sendKeys_Xpath(browser, signup_fnameValue, signup_firstname)
    sendKeys_Xpath(browser, signup_lnameValue, signup_lastname)
    optionfromDrop_text(browser, signup_gender, "Male")
    print('\n\n\n Putting Necessary Credentials >>> DEBUG')


@when('the user clicks on Submit button')
def click_submit(browser):
    clickBy_Xpath(browser, signup_submitBtn)
    print('\n\n\n Submit button clicked >>> DEBUG')


@then('the user logs in to his account')
def afterLogging(browser):
    extractText(browser, signup_accountInfo)
    print('\n\n\n Account info validated >>> DEBUG')


# ------------------------------------

@when('the user writes a text for story')
def writes_text(browser):
    sendKeys_Xpath(browser, story_text, story_textArea)
    print('\n\n\n Story is written >>> DEBUG')


@when('the user clicks on share button')
def clicks_share(browser):
    clickBy_Xpath(browser, story_shareBtn)
    print('\n\n\n Story share button clicked >>> DEBUG')


@then('the story is posted')
def story_posted(browser):
    r = extractText(browser, story_textWritten)
    assert r == story_text, 'Text not same'
    print('\n\n\n Story validated >>> DEBUG')


@when('the user clicks on change profile picture')
def clickChangeDPBtn(browser):
    clickBy_Xpath(browser, changeDP_Btn)
    print('\n\n\n Change Profile Picture button clicked >>> DEBUG')


@when('the user selects the profile picture and upload')
def selectDP(browser):
    sendKeys_Xpath(browser, changeDP_imgPath, changeDP_ChooseFile)
    clickBy_Xpath(browser, changeDP_uploadBtn)
    print('\n\n\n DP selected & upload button clicked >>> DEBUG')


@then('the profile picture is uploaded')
def validateDP(browser):
    wait(5)
    print('\n\n\n Updated DP uploaded >>> DEBUG')


@when('the user deletes the post by a given user')
def deletePost(browser):
    # clickBy_Xpath(browser, deletePost_latest_DeleteBtn)  # deletes the latest post
    clickBy_Xpath(browser, deletePost_particularUser)  # deletes latest post by a user
    print('\n\n\n Post by the selected user deleted >>> DEBUG')


@when('the user searches for a friend')
def searchUsers(browser):
    sendKeys_Xpath(browser, searchFrnd_text, searchFrnd_textBox)
    sendKeys_Xpath(browser, Keys.ENTER, searchFrnd_textBox)
    print('\n\n\n User searched with the text >>> DEBUG')


@then('the user gets a list of account holders')
def searchResults(browser):
    res = extractText_multiple(browser, searchFrnd_result)
    print(res)
    print('\n\n\n Search result here >>> DEBUG')

