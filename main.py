from api.upbit_api import *

# Pythonic approach
# Use dictionary and functions instead of switch-case
# Directly use function names

def show_account_details():
    # Function to fetch account details
    get_account_info()

def check_balance():
    # Profit/loss check functionality - To be implemented
    print("Profit/loss check - To be implemented")
    
def perform_transaction():
    # Transaction performing functionality - To be implemented
    print("Perform transaction - To be implemented")
    
def exit_program():
    # Function to exit the program
    print("The program will exit.")
    exit(0)

def invalid_choice():
    # Handles invalid choices
    print("Invalid choice. Please try again.")
    
def main():
    while True:
        print("\n1. View Assets")
        print("2. Perform Transaction")
        print("3. Check Profit/Loss")
        print("4. Exit")
        
        choice = input("Please choose the desired option: ")

        # switch-case-like structure using dictionary
        switch = {
            '1': show_account_details,
            '2': check_balance,
            '3': perform_transaction,
            '4': exit_program
        }
        
        # Execute the selected action, '4' will exit the program
        action = switch.get(choice, invalid_choice)  # Handles invalid choice
        action()

if __name__ == "__main__":
    main()
