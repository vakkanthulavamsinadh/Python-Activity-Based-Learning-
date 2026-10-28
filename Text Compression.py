Problem Statement:
Compress consecutive repeated characters by writing each character followed by its count, and compare string lengths.

Objectives:
Practise strings, loops, indexing, and run-length encoding.

Assumptions:
Input is a non-empty string. Compression is used for demonstration and may be longer than the original.

Algorithm:
Read a string.
Track the current character and its repetition count.
When the character changes, append the character and count to the compressed string.
Append the final run.
Display original and compressed strings and lengths.

Pseudocode:
START
READ text
compressed ← empty string
i ← 0
WHILE i < length(text)
  count consecutive copies of text[i]
  append text[i] and count to compressed
  move i to next run
DISPLAY text, compressed, lengths
END

Flowchart:
Start → Read text → Count consecutive characters → Append character and count → More characters? → Display compressed text and lengths → End
s = input("Enter a string: ")

python code:
result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count = count + 1
    else:
        result = result + s[i - 1] + str(count)
        count = 1

if len(s) > 0:
    result = result + s[-1] + str(count)

print("Compressed string:", result)

Test Cases:
Input aaabbc → compressed a3b2c1; original length 6; compressed length 6. Input aaaaab → a5b1; original length 6; compressed length 4.

Conclusion:
The program demonstrates run-length encoding and checks whether the encoded representation is shorter.
