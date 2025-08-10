# SAUCEDEMO Automation Framework

## 📌 Overview
This project is a **Selenium + Python + PyTest** automation framework built using the **Page Object Model (POM)** design pattern.  
It automates the end-to-end checkout flow of the [SauceDemo](https://www.saucedemo.com/) application.

The framework is clean, modular, and easily extendable for other e-commerce or web applications.

---

## 🛠 Tech Stack
- **Python 3.13+**
- **PyTest** - test execution & reporting
- **Selenium WebDriver** - browser automation
- **PyTest HTML Plugin** - HTML reports
- **WebDriver Manager** - auto-manages ChromeDriver
- **Jenkins** - CI/CD integration (optional)
- **POM (Page Object Model)** - maintainable structure

---

## 📂 Project Structure
```
SAUCEDEMO_AUTOMATION/
│
├── pages/                  # All Page Objects
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_step_one_page.py
│   ├── checkout_step_two_page.py
│   └── checkout_complete_page.py
│
├── tests/                  # Test scripts
│   ├── test_login.py
│   └── test_checkout_step2.py
│
├── utilities/              # Helper functions
│   └── utils.py
│
├── conftest.py              # Fixtures & Hooks
├── pytest.ini               # PyTest configuration
├── requirements.txt         # Dependencies
└── README.md
```

---

## 🚀 How to Run Tests

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run All Tests
```bash
pytest
```

### 3️⃣ Run a Specific Test
```bash
pytest tests/test_checkout_step2.py
```

### 4️⃣ Run with HTML Report
```bash
pytest --html=reports/report.html
```

---

## ✅ Features
- **End-to-End Checkout Flow**
- **Reusable Page Objects**
- **Custom Logging & Screenshots on Failure**
- **Cross-browser Ready**
- **CI/CD Integration Ready (Jenkins)**

---

## 🖼 Sample Output
Test execution with confirmation message:
```
✅ Order flow completed successfully, confirmation message validated.
```

---

## 🔗 CI/CD Integration
To run this project on **Jenkins**:
1. Install **Python** & dependencies on Jenkins server
2. Configure job with:
   ```bash
   pip install -r requirements.txt
   pytest --html=reports/report.html
   ```
3. Archive the HTML report as a build artifact

---

## 👨‍💻 Author
**Your Name**  
📧 your.email@example.com  
💼 [LinkedIn Profile](https://linkedin.com/in/yourprofile)  
