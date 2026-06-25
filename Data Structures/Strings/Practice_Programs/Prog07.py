# Find the most frequent character in a string.

text = input("Enter a string: ")

freq = {}

for ch in text:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1

max_char = ""
max_count = 0

for ch, count in freq.items():
    if count > max_count:
        max_count = count
        max_char = ch

print("Most frequent character:", max_char)
print("Frequency:", max_count)