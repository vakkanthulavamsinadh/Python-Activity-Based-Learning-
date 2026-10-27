mark1 = int(input("Enter first exam marks: "))
mark2 = int(input("Enter second exam marks: "))

if mark2 > mark1:
    print("Performance improved")
elif mark2 < mark1:
    print("Performance decreased")
else:
    print("Performance unchanged")

print("Difference:", abs(mark2 - mark1))
