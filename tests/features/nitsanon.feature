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

#  @signup
#  Scenario: Basic Nitsanon signup
#    Given the nitsanon home page is displayed
#    When the user clicks on signup button
#    When the user puts neccesary credentials for creating account
#    And the user clicks on Submit button
#    Then the user logs in to his account

#  @story
#  Scenario: Share new story
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    When the user writes a text for story
#    When the user clicks on share button
#    Then the story is posted

#  @ChangeProfilePic
#  Scenario: Change the profile picture
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    When the user clicks on change profile picture
#    And the user selects the profile picture and upload
#    Then the profile picture is uploaded

#  @DeletePost
#  Scenario: Delete the post by spcific user
#    Given the nitsanon home page is displayed
#    When the user puts username and password
#    And the user clicks on Sign In button
#    Then the user logs in successfully
#    When the user deletes the post by a given user

  @SearchFriends
  Scenario: Searches for the users who have account created
    Given the nitsanon home page is displayed
    When the user puts username and password
    And the user clicks on Sign In button
    Then the user logs in successfully
    When the user searches for a friend
    Then the user gets a list of account holders

