# Household Budget Management System

This Python program is a simple and user-friendly command-line application for managing your household budget. It allows you to:

*   Add income and expenses.
*   View all transactions.
*   Filter transactions by category.
*   Analyze expenses by category.
*   Generate monthly or yearly summaries.
*   Save and load budget data from a file.

## Features

*   **Add Transactions:** Easily record income (positive amounts) and expenses (negative amounts) with category and optional descriptions.
*   **View Transactions:** Display all transactions in a well-formatted table, including timestamps, categories, amounts, and descriptions.
*   **Filter Transactions:** View transactions for a specific category.
*   **Expense Analysis:** Get a breakdown of expenses by category to understand your spending habits.
*   **Summaries:** Generate monthly or yearly summaries of income and expenses by category.
*   **Data Persistence:** Save your budget data to a file (`budget_data.txt` by default) so you can load it later.
*   **User-Friendly Interface:** Simple command-line interface with clear prompts.
*   **Error Handling:** Includes error handling to prevent crashes due to invalid input or file issues.

## How to Use

1.  **Prerequisites:** Make sure you have Python 3 installed on your system.
2.  **Download:** Download the `budget_app.py` file.
3.  **Run:** Open a terminal or command prompt, navigate to the directory where you saved the file, and run it using:

    ```bash
    python budget_app.py
    ```

4.  **Interact:** Follow the on-screen prompts to interact with the program.

## File Format

The budget data is stored in a plain text file named `budget_data.txt`. Each line in the file represents a transaction and is formatted as follows:
