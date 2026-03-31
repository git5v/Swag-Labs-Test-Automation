# 🧪 Swag Labs Test Automation

An end-to-end (E2E) automation suite for the [Sauce Demo](https://www.saucedemo.com/) web application. This project leverages **Python**, **Selenium WebDriver**, and **Pytest**.

## 🏗️ Architecture: Page Object Model (POM)
This project implements the **Page Object Model** design pattern to ensure scripts are scalable, maintainable, and readable.


* **`pages/`**: Contains locators and interaction methods. If the UI changes, updates are made here only, leaving test logic untouched.
* **`tests/`**: Contains the test cases and assertions. 
* **`conftest.py`**: A centralized configuration file for Pytest fixtures, handling WebDriver initialization (Setup/Teardown).

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Framework:** Pytest
* **Automation:** Selenium WebDriver
* **Reporting:** Allure Reports

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/git5v/Swag-Labs-Test-Automation.git](https://github.com/git5v/Swag-Labs-Test-Automation.git)
cd Swag-Labs-Test-Automation
```

### 2. Set up a Virtual Environment (Recommended)
**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```
**Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### 🚦 Running Tests
pytest tests/test_login.py
