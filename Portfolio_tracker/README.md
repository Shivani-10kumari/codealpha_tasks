# Stock Portfolio Tracker

A simple Python-based Stock Portfolio Tracker that allows users to calculate the total value of their stock investments using manually defined stock prices.

## Features

* Displays a list of available stocks.
* Takes stock names and quantities as user input.
* Supports adding multiple stocks to the portfolio.
* Calculates the investment value of each stock.
* Handles invalid stock names.
* Displays the total portfolio investment value.

## Technologies Used

* Python 3
* Dictionaries
* Loops
* Conditional Statements
* User Input

## How It Works

1. The program stores predefined stock prices in a Python dictionary.

2. The user enters the number of stocks they want to add.

3. The user enters the stock name and quantity for each stock.

4. The program calculates the investment value using:

   Investment Value = Stock Price × Quantity

5. Finally, the total investment value of the portfolio is displayed.

## Example

```text
=== Stock Portfolio Tracker ===
Available Stocks: AAPL, TSLA, GOOGL, MSFT, AMZN

Enter the number of stocks you want to add: 2

Stock 1
Enter stock name: AAPL
Enter quantity: 5
Investment in AAPL: $900

Stock 2
Enter stock name: TSLA
Enter quantity: 2
Investment in TSLA: $500

=== Portfolio Summary ===
Total Investment Value: $1400
```

## How to Run

1. Make sure Python is installed on your system.
2. Clone or download this repository.
3. Open the project folder in a terminal.
4. Run the Python file:

```bash
python Stock_Portfolio_Tracker.py
```

## Project Purpose

This project was developed as part of a Python programming internship task to demonstrate the practical use of dictionaries, loops, conditional statements, user input, and basic calculations.
