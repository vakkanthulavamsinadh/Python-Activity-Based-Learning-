Problem Statement:
Compare a student's marks across assessments, calculate changes, and identify whether performance improved or declined.

Objectives:
Use lists, loops, averages, and conditions to analyse marks.

Assumptions:
Three assessments are entered, each mark is between 0 and 100. Trends are based on the first and last assessment.

Algorithm:
Read marks for three assessments.
Validate each mark is between 0 and 100.
Calculate changes between consecutive assessments.
Compare first and last marks and display the trend.
Display average marks.

Pseudocode:
START
READ three marks into list
IF any mark outside 0..100: DISPLAY invalid
ELSE calculate average
Calculate second-first and third-second
IF last > first: Improved
ELSE IF last < first: Declined
ELSE: No change
DISPLAY results
END

Flowchart:
Start → Read three marks → Validate → Calculate differences and average → Classify trend → Display → End

python code:
mark1 = int(input("Enter first exam marks: "))
mark2 = int(input("Enter second exam marks: "))

if mark2 > mark1:
    print("Performance improved")
elif mark2 < mark1:
    print("Performance decreased")
else:
    print("Performance unchanged")

print("Difference:", abs(mark2 - mark1))
     
Test Cases:
Marks 60, 70, 80 → average 70; changes +10 and +10; trend Improved. Marks 80, 70, 60 → Declined.

Conclusion:
The program summarises marks and identifies overall performance trends across assessments.
