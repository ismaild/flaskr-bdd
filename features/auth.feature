Feature: As a website owner,
            I want to secure my website

  Scenario: Successful Login
     Given flaskr is setup
      When i login with "admin" and "default"
      Then i should see the alert "You were logged in"

  Scenario: Incorrect Username
     Given flaskr is setup
      When i login with "monty" and "default"
      Then i should see the alert "Invalid username"

  Scenario: Incorrect Password
     Given flaskr is setup
      When i login with "admin" and "python"
      Then  i should see the alert "Invalid password"

  Scenario: Logout
     Given flaskr is setup
     and i login with "admin" and "default"
      When i logout
      Then  i should see the alert "You were logged out"