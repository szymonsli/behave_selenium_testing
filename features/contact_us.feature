Feature: Contact us form
  As a user I want to contact the shop team
  and send them images

  Scenario: sending a contact form without files attached
    Given user visits automationpractice.com Contact Us site
    When user fills in the form with valid email, message and subject
    And clicks submit button
    Then contact form is sent and user sees success alert