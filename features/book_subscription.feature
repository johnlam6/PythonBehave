Feature: WebSocket Book Subscription

  Scenario: Successful subscription to book.BTCUSD-PERP.10
    Given WebSocket connection is established
    When I subscribe to "book.BTCUSD-PERP.10"
    Then I should receive a snapshot response
    And the snapshot should contain 10 bids and 10 asks

  Scenario: Invalid instrument subscription
    Given WebSocket connection is established
    When I subscribe to "book.INVALID.10"
    Then I should receive an error response

  Scenario: Invalid depth subscription
    Given WebSocket connection is established
    When I subscribe to "book.BTCUSD-PERP.100"
    Then I should receive an error response