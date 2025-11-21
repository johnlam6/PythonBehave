# Candlestick Data API & WebSocket Assessment

This repository contains an assessment project completed as part of the application process.  
It demonstrates retrieving candlestick data using the **Crypto.com Exchange REST API** and subscribing to real-time updates using **WebSocket**.

---

## Project Overview

The project includes:

- A REST API client to fetch historical candlestick data
- A WebSocket client to receive live candlestick updates
- Automated tests using the `behave` BDD framework
- Utility modules for logging and data handling

---

## Technologies Used

- Python 3.10  
- `behave`
- `requests`  
- `behave-html-pretty-formatter`
- `websocket-client`
- `datetime`
- `json`

## Project Structure

PythonBehave/
│
├── features/
│ ├── get_candlestick.feature
│ ├── book_subscription.feature
│ ├── environment.py
│ └── steps/
│ ├── candlestick_steps.py
│ └── book_steps.py
│
├── utils/
│ ├── api_helpers.py # REST API logic
│ ├── ws_client.py # WebSocket subscription logic
│ 
├── reports/
│ ├── get_candlestick_report.html
│ └── websocket_report.html
│
├── logs/
│ └── test_log.txt
│
├── behave.ini
├── requirements.txt
└── README.md

##  How to Run the Project

### 1. Clone the Repo

```bash
git clone https://github.com/johnlam6/PythonBehave.git
cd your-repo-name
```

### 2. Set Up the Environment
```bash
python -m venv .venv
.venv\Scripts\activate # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Running Tests
```bash
behave features/get_candlestick.feature
behave features/book_subscription.feature
```

### 5. Generating HTML Report

```bash
 behave .\features\get_candlestick.feature -f behave_html_pretty_formatter:PrettyHTMLFormatter -o .\reports\get_candiestick_report.html
  behave .\features\book_subscription.feature -f behave_html_pretty_formatter:PrettyHTMLFormatter -o .\reports\book_subscription.feature_report.html
 ```

### 6. Checking Test log

```
Open /PythonProject/Logs/test_log.txt
```
