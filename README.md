# CodeAlpha_Tasks
Python Programming Internship Projects | CodeAlpha
# 📈 Stock Portfolio Tracker

<p align="center">
  <b>CodeAlpha Python Programming Internship – Task 2</b>
</p>

## 📌 Project Overview

The **Stock Portfolio Tracker** is a simple console-based Python application developed to calculate the total investment value of a user's stock portfolio.

The application allows users to enter stock symbols and quantities. Using predefined stock prices, it calculates the value of individual stocks and displays the total investment amount.

It also automatically saves the portfolio summary in a text file for future reference.

## 🎯 Project Objectives

- Build a stock portfolio tracking application using Python.
- Understand dictionary operations and data management.
- Accept and process user inputs.
- Perform stock investment calculations.
- Implement file handling to save portfolio reports.

## ✨ Features

- **Predefined Stock Prices:** Stores stock symbols and prices in a Python dictionary.
- **User Input:** Accepts stock symbols and quantities from users.
- **Stock Validation:** Checks whether the entered stock symbol is available.
- **Investment Calculation:** Calculates individual stock values.
- **Total Investment:** Displays the total portfolio investment.
- **Report Generation:** Saves portfolio details automatically in a text file.

## 🛠️ Technologies Used

- Python 3
- Visual Studio Code
- Python Dictionaries
- File Handling

## 📂 Project Structure

```text
CodeAlphaTasks/
│
├── codealphastock_portfolio_tracker.py
├── portfolio.txt
└── README.md
```

## 📊 Available Stocks

The application uses the following predefined stock prices:

| Stock Symbol | Price |
|:---|---:|
| AAPL | ₹180 |
| TSLA | ₹250 |
| GOOGL | ₹140 |
| MSFT | ₹420 |
| AMZN | ₹190 |

**Note:** These are sample stock prices defined manually in the program. They are not live stock market prices.

## ⚙️ How It Works

1. The program displays the available stock symbols and prices.
2. The user enters the number of stocks they want to add.
3. The user enters a stock symbol and its quantity.
4. The program validates the stock symbol.
5. It calculates the individual stock investment value.
6. It calculates and displays the total investment.
7. The portfolio report is saved in `portfolio.txt`.

## 🚀 Installation and Execution

### Prerequisites

- Python 3 installed.
- Visual Studio Code installed.

### Step 1: Clone the Repository

```bash
git clone https://github.com/rojabmrojabm347-jpg/CodeAlpha_StockPortfolioTracker
```

### Step 2: Navigate to the Project Folder

```bash
cd YOUR-REPOSITORY
```

### Step 3: Run the Python Program

```bash
python codealphastock_portfolio_tracker.py
```

### Step 4: View the Report

After successful execution, open `portfolio.txt` to view the saved investment report.

## 💻 Sample Output

```text
========== YOUR PORTFOLIO ==========

AAPL | Quantity: 5 | Price: Rs.180 | Value: Rs.900
TSLA | Quantity: 2 | Price: Rs.250 | Value: Rs.500
MSFT | Quantity: 3 | Price: Rs.420 | Value: Rs.1260

-----------------------------------
Total Investment: Rs.2660
===================================

Portfolio saved successfully!
```

## 🧠 Python Concepts Implemented

| Concept | Application |
|---|---|
| Dictionary | Stores stock prices and portfolio quantities |
| Variables | Stores user inputs and calculations |
| Input/Output | Accepts stock details and displays results |
| Conditional Statements | Validates stock symbols |
| For Loop | Iterates through stock details |
| Arithmetic Operations | Calculates investment values |
| File Handling | Saves the portfolio report |

## 🎓 Internship Details

- **Organization:** CodeAlpha
- **Internship Domain:** Python Programming
- **Task Number:** Task 2
- **Project Name:** Stock Portfolio Tracker

## 👩‍💻 Author

**Roja B M**

Python Programming Intern at CodeAlpha.

---

⭐ If you find this project useful, consider giving this repository a star!

**Thank you for visiting my project!**
