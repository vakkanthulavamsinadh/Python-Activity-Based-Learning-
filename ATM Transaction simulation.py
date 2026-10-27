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
