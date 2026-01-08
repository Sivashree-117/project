def withdraw_cash(balance):
    """
    Handles the ATM withdrawal logic, checking for sufficient balance 
    and amount validity (multiples of 100).
    """
    print(f"Your current balance is: ${balance}")
    
    while True:
        try:
            # Take withdrawal amount as input
            amount = int(input("Enter amount to withdraw (multiples of 100): $"))
            
            # Check if the amount is a multiple of 100
            if amount % 100 != 0:
                print("Error: Amount must be a multiple of 100.")
                continue
            
            # Check if balance is sufficient
            if amount > balance:
                print("Error: Insufficient funds.")
                print(f"You can withdraw up to: ${balance}")
                continue

            # Check if amount is valid (positive)
            if amount <= 0:
                print("Error: Amount must be positive.")
                continue
                
            # Deduct amount and display updated balance
            balance -= amount
            print(f"Withdrawal successful. Please collect your cash.")
            print(f"Your new balance is: ${balance}")
            return balance # Exit function and return the new balance

        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a numeric amount.")

# --- Main part of the program to run the function ---
if __name__ == "__main__":
    # Stores a user's initial balance
    user_balance =int(input("The current balance in your account is:Rs.")) 
    
    # Run the withdrawal function
    user_balance = withdraw_cash(user_balance)

