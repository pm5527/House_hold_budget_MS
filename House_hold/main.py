import datetime
import os

class Budget:
    def __init__(self, filename="budget_data.txt"):
        self.filename = filename
        self.transactions = []
        self.load_from_file()

    def add_transaction(self, category, amount, description=""):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append({"timestamp": timestamp, "category": category, "amount": amount, "description": description})
        self.save_to_file()  # Save after each transaction

    def calculate_balance(self):
        return sum(transaction["amount"] for transaction in self.transactions)

    def display_transactions(self, filter_category=None):
        print("\nTransactions:")
        print("--------------------------------------------------")
        print("{:<20} {:<15} {:<10} {}".format("Timestamp", "Category", "Amount", "Description"))
        print("--------------------------------------------------")

        for transaction in self.transactions:
            if filter_category is None or transaction["category"] == filter_category:
                print("{:<20} {:<15} {:<10.2f} {}".format(transaction["timestamp"], transaction["category"], transaction["amount"], transaction["description"]))
        print("--------------------------------------------------")
        print(f"Current Balance: ₹{self.calculate_balance():.2f}")

    def categorize_expenses(self):
        expenses_by_category = {}
        for transaction in self.transactions:
            if transaction['amount'] < 0:
                category = transaction["category"]
                amount = abs(transaction["amount"])

                expenses_by_category.setdefault(category, 0) # cleaner way to initialize
                expenses_by_category[category] += amount

        print("\nExpense Breakdown:")
        for category, total in expenses_by_category.items():
            print(f"- {category}: ₹{total:.2f}")

    def generate_summary(self, period="monthly"):  # New feature: Summary
        if not self.transactions:
            print("No transactions to summarize.")
            return

        now = datetime.datetime.now()
        if period == "monthly":
            start_date = now.replace(day=1)
        elif period == "yearly":
            start_date = now.replace(month=1, day=1)
        else:
            print("Invalid period. Choose 'monthly' or 'yearly'.")
            return

        summary = {}
        for transaction in self.transactions:
            transaction_date = datetime.datetime.strptime(transaction['timestamp'], "%Y-%m-%d %H:%M:%S")

            if start_date <= transaction_date <= now:
                category = transaction['category']
                amount = transaction['amount']
                summary.setdefault(category, {'income': 0, 'expenses': 0})

                if amount > 0:
                    summary[category]['income'] += amount
                else:
                    summary[category]['expenses'] += abs(amount)

        print(f"\n{period.capitalize()} Summary ({start_date.strftime('%Y-%m-%d')} - {now.strftime('%Y-%m-%d')}):")
        for category, data in summary.items():
            print(f"- {category}: Income: ₹{data['income']:.2f}, Expenses: ₹{data['expenses']:.2f}")

    def save_to_file(self):
        try:
            with open(self.filename, "w") as f:
                for transaction in self.transactions:
                    f.write(f"{transaction['timestamp']},{transaction['category']},{transaction['amount']},{transaction['description']}\n")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self):
        try:
            if os.path.exists(self.filename): # check if file exists before trying to open it
                with open(self.filename, "r") as f:
                    self.transactions = []
                    for line in f:
                        parts = line.strip().split(",")
                        if len(parts) == 4:
                            timestamp, category, amount, description = parts
                            try:
                                amount = float(amount)
                                self.transactions.append({"timestamp": timestamp, "category": category, "amount": amount, "description": description})
                            except ValueError:
                                print(f"Skipping invalid amount in line: {line.strip()}")
            else:
                print(f"File {self.filename} not found. Starting with a new budget.")

        except Exception as e:
            print(f"Error loading from file: {e}")


def main():
    budget = Budget()

    while True:
        print("\nHousehold Budget Management System")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Filter Transactions by Category")  # New: Filter transactions
        print("5. Analyze Expenses by Category")
        print("6. Generate Summary (Monthly/Yearly)") # New: Generate summary
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1" or choice == "2":
                category = input("Enter category (e.g., Salary, Rent, Groceries): ")
                while True:
                    try:
                        amount = float(input("Enter amount (positive for income, negative for expense): "))
                        break
                    except ValueError:
                        print("Invalid amount. Please enter a number.")
                description = input("Enter description (optional): ")
                budget.add_transaction(category, amount, description)
                print("Transaction added successfully!")

            elif choice == "3":
                budget.display_transactions()

            elif choice == "4": # Filter
                filter_category = input("Enter category to filter by (or press Enter for all): ")
                budget.display_transactions(filter_category)

            elif choice == "5":
                budget.categorize_expenses()

            elif choice == "6": # Summary
                period = input("Enter summary period (monthly/yearly): ").lower()
                budget.generate_summary(period)

            elif choice == "7":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()