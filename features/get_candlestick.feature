Feature: Get Candlestick Data from Crypto.com Exchange

  Scenario Outline: Valid candlestick data retrieval
    Given the instrument name is "<instrument_name>"
    And the timeframe is "<timeframe>"
    When I call the public/get-candlestick endpoint
    Then the response code should be 0
    And the response should contain candlestick data

    Examples:
      | instrument_name | timeframe |
      | BTCUSD-PERP     | 1m        |
      | ETHUSD-PERP     | 1h        |
      | BTC_USDT        | 1D        |

  Scenario: Missing instrument name
    Given the instrument name is "xxx"
    And the timeframe is "M5"
    When I call the public/get-candlestick endpoint
    Then the response code should not be 0

  Scenario: Invalid timeframe
    Given the instrument name is "BTCUSD-PERP"
    And the timeframe is "Z9"
    When I call the public/get-candlestick endpoint
    Then the response code should not be 0