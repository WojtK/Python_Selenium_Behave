Feature: sign in to my account
  As a user I want to log in
  and have access to Orange TV Go service

  Scenario Outline: Log in with valid data
    Given  user is on Orange TV Go website
    When  user fills valid username <username> and valid password <password> and submits it
    Then  user can see my zone

    Examples:
      | username | password |
      | 9999999088 | 4365   |
      | 9999999086 | 9474   |

  Scenario Outline: Log in with invalid data
    Given user is on Orange TV Go website
    When user fills invalid username <invalidusername> and/or invalid password <invalidpassword> and submits it
    Then User can see alert about invalid data
    Examples:
      |invalidusername | invalidpassword |
      | 9999999088 | 1111 |
      | 9999999089 | 1111 |
      | 9999999999 | 4365 |

    Scenario Outline: Logout
      Given user is on Orange TV Go website
      When user fills valid username <username> and valid password <password> and submits it
      Then User logout
      Examples:
        | username | password |
        | 9999999088 | 4365   |
        | 9999999086 | 9474   |