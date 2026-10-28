Problem Statement:
Check whether a password satisfies basic rules for length, uppercase, lowercase, digit, and special character.

Objectives:
Practise string operations, loops, flags, and conditions.

Assumptions:
A valid password must contain at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character.

Algorithm:
Read the password.
Check its length.
Loop through characters and detect uppercase, lowercase, digit, and special character.
Display each failed rule or a success message.

Pseudocode:
START
READ password
Set uppercase, lowercase, digit, special flags to false
FOR each character in password: update flags
Check length ≥ 8 and all flags
IF all conditions true: DISPLAY valid
ELSE DISPLAY failed rules
END

Flowchart:
Start → Read password → Check length and character types → Any rule failed? → Show errors / Valid password → End
python code:
password = input("Enter password: ")
digit = False

for ch in password:
    if ch.isdigit():
        digit = True

if len(password) >= 8 and digit:
    print("Valid password")
else:
    print("Invalid password")
    
Test Cases:
Abcd123! → valid. abc123 → fails length, uppercase, and special-character rules.

Conclusion:
The program validates password structure and gives the user clear feedback about missing requirements.
