Problem Statement:
Compare a student's answers with an answer key and calculate correct, incorrect, unanswered, and final marks.

Objectives
Use lists, loops, string comparison, and arithmetic to evaluate answers.

Assumptions:
There are five questions. Each correct answer earns 2 marks; each incorrect answer loses 0.5 marks; blank answers receive zero.

Algorithm:
Store the answer key in a list.
Read five answers, using a blank string for unanswered questions.
Compare each answer with the key and update counts and score.
Display counts and final score.

Pseudocode:
START
key ← [A, B, C, D, A]
correct, wrong, blank, score ← 0
FOR each question
  READ answer
  IF answer blank: blank += 1
  ELSE IF answer equals key: correct += 1; score += 2
  ELSE: wrong += 1; score -= 0.5
DISPLAY counts and score
END

Flowchart:
Start → Set answer key and marks → Read answers → Compare each answer → Update score and counts → Display result → End
key = ["A", "B", "C", "D", "A"]
answers = []

python code:
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

Test Cases:
Key A,B,C,D,A; answers A,B,blank,D,C → correct 2, incorrect 2, unanswered 1, score 3.0.

Conclusion:
The program evaluates answers consistently and reports the result using a simple negative-marking policy.
