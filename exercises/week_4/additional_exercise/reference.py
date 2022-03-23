letter_count = {}

words = []
with open("5_letter_words.txt") as f:
    for line in f:
        words.append(line.strip())

for word in words:
    for char in word:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

most_common = ("", 0)
for item in letter_count.items():
    if item[1] > most_common[1]:
        most_common = item

words_with_most_common_letter = 0
for word in words:
    if most_common[0] in word:
        words_with_most_common_letter += 1

print(f"The most common letter is {most_common[0]}. It occurs {most_common[1]} times.")
print(f"There are {words_with_most_common_letter} words containing this letter.")
