#attendence recovery computation
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









































