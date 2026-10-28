Problem Statement:

Simulate deposits and withdrawals, maintain the account balance, reject invalid transactions, and display a transaction summary.

Objectives:

Use variables, conditional statements, loops, and arithmetic operators to process transactions safely.

Assumptions:

Opening balance is ₹5,000. Deposit and withdrawal amounts must be positive. A withdrawal cannot exceed the available balance.

Algorithm:

Start with balance = 5000 and transaction counters = 0.

Display a menu for deposit, withdrawal, balance, and exit.

Read the user's choice and process it using conditions.

Reject non-positive amounts and withdrawals greater than the balance.

Update counters and balance for valid transactions.

Display the final summary and stop when Exit is selected.

Pseudocode:

START
balance ← 5000
REPEAT
  DISPLAY menu; READ choice
  IF choice = 1: READ amount; if amount > 0, add to balance
  ELSE IF choice = 2: READ amount; if 0 < amount ≤ balance, subtract
  ELSE IF choice = 3: DISPLAY balance
  ELSE IF choice = 4: DISPLAY summary; EXIT LOOP
  ELSE: DISPLAY invalid choice
UNTIL exit
END

Flowchart

Start → Set opening balance → Display menu → Read choice → Deposit / Withdraw / Check balance → Update or show error → Repeat? → Show summary → End

Python Source Code:
balance = 1000

deposit = int(input("Enter deposit amount: "))
balance = balance + deposit

withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal successful")
else:
    print("Insufficient balance")

print("Final balance:", balance)
Test Cases:
Deposit ₹1,000 → balance ₹6,000; withdraw ₹500 → balance ₹5,500; withdraw ₹9,000 → rejected; deposit ₹0 → rejected.

Conclusion:
The program simulates basic ATM operations and validates transactions before updating the balance
