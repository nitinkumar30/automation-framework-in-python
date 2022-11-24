@nitsanon
Feature: Nitsanon Web Browsing
  As a web surfer,
  I want to login in here.

  
#  @login
#  Scenario: Basic Nitsanon login
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    And the user logs out by clicking logout button


#  @signup
#  Scenario: Basic Nitsanon signup
#    Given the nitsanon home page is displayed
#    When the user clicks on signup button
#    When the user puts neccesary credentials for creating account
#    And the user clicks on Submit button
#    Then the user logs in to his account
#    And the user logs out by clicking logout button


#  @story
#  Scenario: Share new story
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    When the user writes a text for story
#    When the user clicks on share button
#    Then the story is posted
#    And the user logs out by clicking logout button


#  @ChangeProfilePic
#  Scenario: Change the profile picture
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    When the user clicks on change profile picture
#    And the user selects the profile picture and upload
#    Then the profile picture is uploaded
#    And the user logs out by clicking logout button


#  @DeletePost
#  Scenario: Delete the post by spcific user
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    When the user deletes the post by a given user
#    And the user logs out by clicking logout button


#  @SearchFriends
#  Scenario: Searches for the users who have account created
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    When the user searches for a friend
#    Then the user gets a list of account holders
#    And the user logs out by clicking logout button


#  @SendFriendRequest
#  Scenario: Searches for the users and send them friend requests with a particular name
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    When the user searches for a friend
#    Then the user gets a list of account holders
##    When the user clicks on add as friend besides a user
##    Then the user should be a friend now
#    When the user clicks on unfriend besides a user
#    And the user logs out by clicking logout button


#  @UploadNewImage
#  Scenario: Uploads a new image in user account
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    When the user navigates to photos tab
#    And uploads an image into his account
##    Then image should gets uploaded
#    And the user logs out by clicking logout button


#@Logout
#  Scenario: Edit user profile in portal
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    And the user logs out by clicking logout button


  @editProfile
  Scenario: Logout functionality in portal
    Given the nitsanon home page is displayed
    When the user puts username and password
    And the user clicks on Sign In button
    Then the user logs in successfully
    When the user navigates to profile tab
    Then the user clicks on Edit button
    And edit the changes need to be made
    When the user navigates to profile tab
    Then the user logs out by clicking logout button


#  @messageFrnd
#  Scenario: Message a friend in portal
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    When the user navigates to Message tab # not written
#    Then the user selects the friend # not written
#    And the user writes the message and click on Send # not written
#    When the user navigates to profile tab
#    Then the user logs out by clicking logout button


