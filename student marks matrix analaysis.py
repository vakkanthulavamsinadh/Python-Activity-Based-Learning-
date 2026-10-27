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
