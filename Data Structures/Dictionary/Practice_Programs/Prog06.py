# Group words by their first letter using a dictionary:
# ["apple", "ant", "ball", "cat"] → {"a": ["apple", "ant"], "b": ["ball"], "c": ["cat"]}

my_list = ["apple", "Ant", "ball", "Bat", "cat"]

groups = {}

for word in my_list:
    first_letter = word[0].lower()

    if first_letter not in groups:
        groups[first_letter] = []

    groups[first_letter].append(word)

print(groups)
