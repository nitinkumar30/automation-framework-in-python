# NITSANON

# login
login_loginBtn = "//a[@class='to_register']"
login_userInput = "//input[@id='username']"
login_passInput = "//input[@id='password']"
login_submitBtn = "//input[@name='login']"

# Signup

signup_Btn = "//a[@class='to_register']"
signup_userInput = "//input[@id='usernamesignup']"
signup_passInput = "//input[@id='passwordsignup']"
signup_firstname = "//input[@name='firstname']"
signup_lastname = "//input[@name='lastname']"
signup_gender = "//*[@name='gender']"
signup_submitBtn = "//*[@id='register']/form/p[6]/input"
signup_accountInfo = "//*[@id='masthead']/div[1]/div/div[2]/p[2]"

# Share story
story_textArea = "//*[@id='masthead']/div[1]/div/div[3]/form/textarea"
story_shareBtn = "//*[@id='masthead']/div[1]/div/div[3]/form/button"
story_textWritten = "/html/body/div[2]/div/div/div/div/div/div[2]/div[1]"

# Change profile picture
changeDP_Btn = "//*[@id='masthead']/div[1]/div/div[1]/a"
changeDP_ChooseFile = "//input[@name='image']"
changeDP_uploadBtn = "//button[@name='submit']"

# Delete latest post
deletePost_fullName = 'Black Eagle'
deletePost_latest_DeleteBtn = "//div[2]/a/i"
deletePost_user = "//a[contains(text(),'Nitin kumar')]"
deletePost_particularUser = "//a[contains(text(),'" + deletePost_fullName + "')]/ancestor::div/div/div/div/div/div[2]/div[2]/child::div[2]/a "

# Profile option from navigation
navOption_profile = "//a[contains(text(),'Profile')]"
navOption_photos = "//a[contains(text(),'Photos')]"
navOption_friends = "//a[contains(text(),'Friends')]"
navOption_message = "//a[contains(text(),'Message')]"
navOption_logout = "//a[contains(text(),'Logout')]"

# Search friend
searchFrnd_textBox = "//input[@name='search']"
searchFrnd_text = "Nitin"
searchFrnd_result = "//div[@class='alert']"

