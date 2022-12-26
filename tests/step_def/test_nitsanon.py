from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.framework.functions import *
from tests.framework.variables import *
from tests.framework.xpaths import *

# Scenarios import

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
    emptyDirectory(browser, './evidences/')
    yield b
    b.quit()


# Given Steps implementations

@given('the nitsanon home page is displayed')
def ddg_home(browser):
    browser.get(nitsanonURL)
    screenshot(browser, 'homepage_displayed')
    print('\n\n\nOpen Browser >>> DEBUG')


@when('the user puts username and password')
def input_credentials(browser):
    browser.implicitly_wait(5)
    sendKeys_Xpath(browser, userValue, login_userInput)
    sendKeys_Xpath(browser, passValue, login_passInput)
    screenshot(browser, 'credentials_given')
    print('\n\n\n Credentials given >>> DEBUG')


@when('the user clicks on Sign In button')
def clicks_submit(browser):
    clickBy_Xpath(browser, login_submitBtn)
    screenshot(browser, 'loginBtn_clicked')
    print('\n\n\n Clicked >>> DEBUG')


@then('the user logs in successfully')
def logs_in(browser):
    links_div = browser.find_element(By.CLASS_NAME, "row")
    links_div.is_displayed()
    screenshot(browser, 'loggedIn')
    print('\n\n\n After logging In >>> DEBUG')


@when('the user clicks on signup button')
def clicks_signup(browser):
    clickBy_Xpath(browser, signup_Btn)
    screenshot(browser, 'signUpBtn_clicked')
    print('\n\n\n Signup Button clicked >>> DEBUG')


@when('the user puts neccesary credentials for creating account')
def input_credentials(browser):
    sendKeys_Xpath(browser, signup_userValue, signup_userInput)
    screenshot(browser, 'usernameInput')
    sendKeys_Xpath(browser, signup_passValue, signup_passInput)
    screenshot(browser, 'passwordInput')
    sendKeys_Xpath(browser, signup_fnameValue, signup_firstname)
    screenshot(browser, 'firstnameInput')
    sendKeys_Xpath(browser, signup_lnameValue, signup_lastname)
    screenshot(browser, 'lastnameInput')
    optionfromDrop_text(browser, signup_gender, "Male")
    screenshot(browser, 'genderInput')
    print('\n\n\n Putting Necessary Credentials >>> DEBUG')


@when('the user clicks on Submit button')
def click_submit(browser):
    clickBy_Xpath(browser, signup_submitBtn)
    screenshot(browser, 'submitBtn_clicked')
    print('\n\n\n Submit button clicked >>> DEBUG')


@then('the user logs in to his account')
def afterLogging(browser):
    extractText(browser, signup_accountInfo)
    screenshot(browser, 'accountInfo')
    print('\n\n\n Account info validated >>> DEBUG')


@when('the user writes a text for story')
def writes_text(browser):
    sendKeys_Xpath(browser, story_text, story_textArea)
    screenshot(browser, 'storyText')
    print('\n\n\n Story is written >>> DEBUG')


@when('the user clicks on share button')
def clicks_share(browser):
    clickBy_Xpath(browser, story_shareBtn)
    screenshot(browser, 'shareBtn_clicked')
    print('\n\n\n Story share button clicked >>> DEBUG')


@then('the story is posted')
def story_posted(browser):
    r = extractText(browser, story_textWritten)
    assert r == story_text, 'Text not same'
    screenshot(browser, 'storyPosted_validation')
    print('\n\n\n Story validated >>> DEBUG')


@when('the user clicks on change profile picture')
def clickChangeDPBtn(browser):
    clickBy_Xpath(browser, changeDP_Btn)
    screenshot(browser, 'changeDPBtn_clicked')
    print('\n\n\n Change Profile Picture button clicked >>> DEBUG')


@when('the user selects the profile picture and upload')
def selectDP(browser):
    sendKeys_Xpath(browser, changeDP_imgPath, changeDP_ChooseFile)
    screenshot(browser, 'imagePath_provided')
    clickBy_Xpath(browser, changeDP_uploadBtn)
    screenshot(browser, 'changeDPBtn_clicked')
    print('\n\n\n DP selected & upload button clicked >>> DEBUG')


@then('the profile picture is uploaded')
def validateDP(browser):
    wait(5)
    screenshot(browser, 'DPUploaded')
    print('\n\n\n Updated DP uploaded >>> DEBUG')


@when('the user deletes the post by a given user')
def deletePost(browser):
    # clickBy_Xpath(browser, deletePost_latest_DeleteBtn)  # deletes the latest post
    clickBy_Xpath(browser, deletePost_particularUser)  # deletes latest post by a user
    screenshot(browser, 'deletesPost')
    print('\n\n\n Post by the selected user deleted >>> DEBUG')


@when('the user searches for a friend')
def searchUsers(browser):
    sendKeys_Xpath(browser, searchFrnd_text, searchFrnd_textBox)
    screenshot(browser, 'searchesForFrnd')
    sendKeys_Xpath(browser, Keys.ENTER, searchFrnd_textBox)
    screenshot(browser, 'homepage_displayed')
    print('\n\n\n User searched with the text >>> DEBUG')


@then('the user gets a list of account holders')
def searchResults(browser):
    res = extractText_multiple(browser, searchFrnd_result)
    print(res)
    print('\n\n\n Search result here >>> DEBUG')


@when('the user clicks on add as friend besides a user')
def sendFrndReq(browser):
    res, xp = clickBtn_multiple(browser, sendReq_addFrndBtn)
    print('\n\n\n Sent Friend Request to all users with mentioned name >>> DEBUG\n', res, xp)


@then('the user should be a friend now')
def frndVerified(browser):
    clickBy_Xpath(browser, navOption_friends)
    res = extractText_multiple(browser, searchFrnd_result)
    print('Value of res is -', res)


@when('the user clicks on unfriend besides a user')
def sendFrndReq(browser):
    res, xp = clickBtn_multiple(browser, unfrnd_Btn)
    print('\n\n\n Unfriended to all users with mentioned name >>> DEBUG\n', res, xp)


@when('the user navigates to photos tab')
def navigatePhotos(browser):
    clickBy_Xpath(browser, navOption_photos)
    print('\n\n\n Navigated to Photos TAB >>> DEBUG\n')


@when('uploads an image into his account')
def uploadImg(browser):
    sendKeys_Xpath(browser, changeDP_imgPath, changeDP_ChooseFile)
    clickBy_Xpath(browser, changeDP_uploadBtn)
    print('\n\n\n Image selected & upload button clicked >>> DEBUG')


@then('the user logs out by clicking logout button')
def logout(browser):
    clickBy_Xpath(browser, navOption_logout)
    screenshot(browser, 'logoutBtn_clicked')
    print('\n\n\n Logout button clicked >>> DEBUG')


@when('the user navigates to profile tab')
def navigatePhotos(browser):
    clickBy_Xpath(browser, navOption_profile)
    print('\n\n\n Navigated to Profile TAB >>> DEBUG\n')


@then('the user clicks on Edit button')
def clickEditBtn(browser):
    clickBy_Xpath(browser, profile_EditBtn)
    print('\n\n\n Edit button clicked >>> DEBUG')


@then('edit the changes need to be made')
def editProfile(browser):
    # sendKeys_Xpath(browser, edit_username, profile_username)  # For changing username
    sendKeys_Xpath(browser, edit_firstname, profile_firstname)  # For changing firstname
    # sendKeys_Xpath(browser, edit_lastname, profile_lastname)  # For changing lastname
    # optionfromDrop_text(browser,profile_gender, edit_gender)  # For changing gender
    # sendKeys_Xpath(browser, edit_birthdate, profile_birthdate)  # For changing birthdate
    # sendKeys_Xpath(browser, edit_address, profile_address)  # For changing address
    # sendKeys_Xpath(browser, edit_status, profile_status)  # For changing status
    # sendKeys_Xpath(browser, edit_mobile, profile_mobile)  # For changing mobile
    # sendKeys_Xpath(browser, edit_work, profile_work)  # For changing work
    # sendKeys_Xpath(browser, edit_religion, profile_religion)  # For changing religion
    clickBy_Xpath(browser, profile_saveBtn)
    print('\n\n\n Profile updated successfully >>> DEBUG')


@when('the user navigates to Message tab')
def navigateMsg(browser):
    clickBy_Xpath(browser, navOption_message)
    print('\n\n\n Navigated to Messages TAB >>> DEBUG\n')


@then('the user selects the friend')
def selectFrnd(browser):

    print('\n\n\n User is selected successfully >>> DEBUG\n')


