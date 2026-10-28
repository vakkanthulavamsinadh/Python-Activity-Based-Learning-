1. Problem Statement:
Write a Python program to store marks of three students in three subjects using a nested list. Calculate and display the total marks and average marks for each student.
2. Objectives
- To understand nested lists in Python.
- To accept and store student marks.
- To calculate total and average marks.
- To display student-wise results using loops.
3. Assumptions
- There are three students and three subjects.
- Marks are entered as integers.
- Each student has marks for all three subjects.
- The program calculates totals and averages out of three subjects.
4. Algorithm
1. Start the program.
2. Create an empty list named marks.
3. Use nested loops to read marks for three students in three subjects.
4. Store each student's marks in a separate list.
5. Calculate the total marks of each student using sum().
6. Calculate the average by dividing the total by 3.
7. Display each student's total and average marks.
8. Stop the program.
5. Flowchart
Start
Initialize empty marks list

Input marks using nested loops
Store marks in nested list
Calculate total and average for each student
Display student-wise results
Stop

python code:
marks = []

for i in range(3):
    row = []
    for j in range(3):
        m = int(input("Enter marks: "))
        row.append(m)
    marks.append(row)

for i in range(3):
    total = sum(marks[i])
    average = total / 3

    print("Student", i + 1)
    print("Total:", total)
    print("Average:", average)
    
pseudo code:
START
marks = empty list
FOR i = 0 TO 2
    row = empty list
    FOR j = 0 TO 2
        INPUT m
        ADD m TO row
    END FOR
    ADD row TO marks
END FOR

FOR i = 0 TO 2
    total = SUM(marks[i])
    average = total / 3
    PRINT student number
    PRINT total
    PRINT average
END FOR
STOP
test cases:
Student 	Subject 1	Subject 2	Subject 3	Total	Average
1	          80	      70	      90	     240	80.0
2	          60	      75	      65	     200	66.67
3	          85	      90	      95	     270	90.0
sample output:
Student 1
Total: 240
Average: 80.0

Student 2
Total: 200
Average: 66.66666666666667

Student 3
Total: 270
Average: 90.0

Conclusion
The program successfully stores student marks using nested lists and calculates the total and average marks for each student. It demonstrates the use of nested loops, lists, and basic arithmetic operations in Python.
