Problem Statement:
Calculate current attendance and find the minimum consecutive classes a student must attend to reach a required attendance percentage.

Objectives:
Use arithmetic and a loop to calculate attendance recovery requirements.

Assumptions:
The student attends every future class. Required attendance is 75%. Classes already conducted must be greater than zero.

Algorithm:
Read classes attended and total classes conducted.
Validate the values.
Calculate current attendance percentage.
If below 75%, add one future attended class at a time until the percentage reaches 75%.
Display current percentage and required classes.

Pseudocode:
START
READ attended, total
IF total ≤ 0 or attended < 0 or attended > total: DISPLAY invalid
current ← attended / total × 100
future ← 0
WHILE (attended + future) / (total + future) × 100 < 75
future ← future + 1
DISPLAY current and future
END

Flowchart:
Start → Read attended and total classes → Validate → Calculate percentage → Already eligible? → Yes: 0 classes / No: loop future classes until target → Display → End

python code:
attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes: "))

percentage = attended / total * 100
print("Attendance:", percentage, "%")

if percentage >= 75:
    print("Eligible")
else:
    needed = 0
    while (attended + needed) / (total + needed) * 100 < 75:
        needed = needed + 1
    print("Classes needed:", needed)
Test Cases:
Attended 60 out of 100 → current 60%; attend 60 consecutive classes to reach 75% (120/160 = 75%). Attended 80 out of 100 → current 80%; required future classes 0.

Conclusion:
The program computes current attendance and the minimum future classes needed to meet the target if every upcoming class is attended.
































