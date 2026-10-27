attendance = int(input("Enter attendance percentage: "))
lab = int(input("Enter completed labs (out of 10): "))
marks = int(input("Enter internal marks: "))

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
