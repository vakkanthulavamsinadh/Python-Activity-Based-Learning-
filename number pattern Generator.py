1. Problem Statement
Write a Python program to generate a number pattern based on the number of rows entered by the user. Each row displays numbers starting from 1 up to the row number.

2. Objectives
- To understand nested loops in Python.
- To generate number patterns using for loops.
- To accept input from the user.
- To use the print() function to display the pattern.

3. Assumptions
- The user enters a positive integer for the number of rows.
- The pattern starts from row 1.
- Each row prints numbers from 1 up to the current row number.

4. Algorithm
1. Start the program.
2. Read the number of rows from the user.
3. Use an outer loop from 1 to the number of rows.
4. Use an inner loop to print numbers from 1 to the current row number.
5. Move to the next line after printing each row.
6. Stop the program.

5. Flowchart
Start
Input number of rows n
Outer loop: i = 1 to n
Inner loop: print j from 1 to i
Move to next line
End

python code:
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
pseudo code:
START
INPUT n
FOR i = 1 TO n
    FOR j = 1 TO i
        PRINT j without newline
    END FOR
    PRINT newline
END FOR
STOP

test cases:
Input	Expected output
3	         1
             1 2
             1 2 3

4         	 1
             1 2
             1 2 3
             1 2 3 4
1        	1

Conclusion:
The program successfully generates a number pattern using nested for loops. It demonstrates user input, iteration, and formatted output in Python.
