# Bitcoin Price Automation Project

## Overview

This project automates the process of:
- Fetching the current Bitcoin Price Index (BPI) from a public API every minute for one hour
- Logging all actions and errors
- Saving the collected prices to a JSON file
- Generating a graph of the price changes over the hour
- Sending an email with the maximum price and the graph attached

The project uses Object-Oriented Programming (OOP) principles and is modular for clarity and maintainability.

---

## Project Structure

```
exc1/
│
├── main.py                # Main execution script
├── config.py               # Configuration file (API URL, SMTP credentials, etc.)
├── instructions.txt        # Task instructions
├── README.md               # Project documentation
├── bitcoin_prices.json     # Output: Collected Bitcoin prices (generated after run)
├── bitcoin_bpi.png         # Output: Price graph image (generated after run)
├── bitcoin_price.log       # Output: Log file (generated after run)
│
├── utils/                  # Core logic modules (OOP classes)
│   ├── __init__.py
│   ├── logger.py
│   ├── fetcher.py
│   ├── data_collector.py
│   ├── grapher.py
│   └── emailer.py
│
├── tests/                  # Unit tests for project modules
│   ├── __init__.py
│   ├── conftest.py         # Shared fixtures (e.g., logger)
│   ├── test_fetcher.py     # Tests for fetching logic
│   ├── test_grapher.py     # Tests for graphing logic
│   └── test_emailer.py     # Tests for emailing logic
│
└── (auto-generated folders like __pycache__ and .pytest_cache can be ignored/deleted)
```

---

## How to Run

1. **Configure your settings:**  
   Edit `config.py` and fill in your email credentials and recipient address.  
   **Important:** Do NOT share real credentials; use placeholders if sharing the code.

2. **Run the main script:**  
   ```bash
   python main.py
   ```
   - This will fetch prices, generate the graph, and send the email.

3. **Check outputs:**  
   - `bitcoin_prices.json` — Collected data
   - `bitcoin_bpi.png` — Graph image
   - `bitcoin_price.log` — Log file

---

## Unit Testing

- The `tests` folder contains unit tests for the project’s main components.
- Each test file targets a specific module (fetching, graphing, emailing).
- To run all tests:
  ```bash
  pytest
  ```
- These tests help ensure the reliability of the project’s core logic.

---

## Notes

- The main execution script is `main.py`.
- The `tests` folder is for unit testing only and does not affect the main script.
- Ignore or delete `__pycache__` and `.pytest_cache` folders before sharing or submitting the project.

---