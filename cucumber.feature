Feature: User authentication

Scenario: User is not authenticated
    Given I am on the login page
    When I fill in the username field with "user"
    And I fill in the password field with "<PASSWORD>"
    And I click on the login button
    Then I should see the login page
    And I should see the "You are not logged in" message

Scenario: User login with valid credentials
    Given I am on the login page
    When I fill in the username field with "user"
    And I fill in the password field with "<PASSWORD>"
    And I click on the login button
    Then I should see the login page
    And I should see the "You are logged in" message

Scenario: User forgot password
    Given I am on the login page
    When I fill in the username field with "user"
    And I fill in the password field with "<PASSWORD>"
    And I click on the forgot password button
    Then I should see the forgot password page
    And I should see the "Please enter your email address" message
    And I should see the "Please enter your password" message
    And I should see the "Please enter your password again" message
    And I should see the "Please enter your email address" message
    And I should see the "Please enter your email address again" message
    And I should see the "Please enter your password" message
    And I should see the "Please enter your password again" message
    And I should see the "Please enter your email address" message
    And I should see the "Please enter your email address again" message
    And I should see the "Please enter your password" message
    And I should see the "Please enter your password again" message
    And I should see the "Please enter your email address" message
    And I should see the "Please enter your email address again" message
    And I should see the "Please enter your password" message
    And I should see the "Please enter your
    