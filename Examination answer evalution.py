key = ["A", "B", "C", "D", "A"]
answers = []

for i in range(5):
    a = input("Enter answer: ").upper()
    answers.append(a)

correct = 0
wrong = 0

for i in range(5):
    if answers[i] == key[i]:
        correct = correct + 1
    elif answers[i] != "":
        wrong = wrong + 1

print("Correct answers:", correct)
print("Wrong answers:", wrong)
print("Total marks:", correct)
