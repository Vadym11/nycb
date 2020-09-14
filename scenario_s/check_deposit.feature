Feature: Verify "pay deposit" option
  Verify that "pay deposit" option has been applied

  Scenario: Apply "pay deposit" option
    Given I am on the main page with having menu opened
    When I click on the "all wedding dresses" link
    When I click on first product in the list
    When I click on the "Pay deposit" button
    When I click on the "Add to cart" button
    When I click on the "View cart" button
    Then "payable in total" text is against product name in the cart