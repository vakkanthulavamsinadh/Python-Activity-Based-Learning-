Problem Statement:
Determine whether a student can attend the final examination using attendance, laboratory completion, internal marks, and fee-clearance conditions.

Objectives:
Apply multiple conditions and report every unmet eligibility requirement.

Assumptions:
Eligibility requires attendance of at least 75%, completed laboratory work, internal marks of at least 40 out of 100, and cleared fees.

Algorithm:
Read attendance percentage, lab status, internal marks, and fee status.
Check each requirement separately.
Store and display every failed requirement.
If none fail, display Eligible; otherwise display Not Eligible.

Pseudocode:
START
READ attendance, lab_done, internal_marks, fees_paid
reasons ← empty list
IF attendance < 75: add attendance reason
IF lab_done is false: add lab reason
IF internal_marks < 40: add marks reason
IF fees_paid is false: add fee reason
IF reasons empty: DISPLAY Eligible
ELSE: DISPLAY Not Eligible and reasons
END

Flowchart:
Start → Read student details → Check attendance, lab, marks, fees → Any condition failed? → List failures / Eligible → End
attendance = int(input("Enter attendance percentage: "))
lab = int(input("Enter completed labs (out of 10): "))
marks = int(input("Enter internal marks: "))

python source code:
if attendance >= 75 and lab == 10 and marks >= 20:
    print("Eligible for examination")
else:
    print("Not eligible for examination")

    if attendance < 75:
        print("Low attendance")
    if lab < 10:
        print("Laboratory incomplete")
    if marks < 20:
        print("Low internal marks")
Test Cases:
Attendance 80, lab yes, marks 65, fees yes → Eligible. Attendance 60, lab no, marks 30, fees no → Not eligible; all four reasons displayed.

Conclusion:
The program checks all specified eligibility rules and explains which requirements are unmet.
