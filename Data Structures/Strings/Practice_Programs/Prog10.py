#Count how many times a specific word appears in a paragraph

paragraph = input("Enter a paragraph:\n")
search_word = input("Enter the word to search: ")

words = paragraph.lower().split()
search_word = search_word.lower()

count = 0

for word in words:
    if word == search_word:
        count += 1

print(f"'{search_word}' appears {count} times.")