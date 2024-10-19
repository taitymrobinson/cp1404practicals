"""
CP1404 PRAC 05
Word Occurrences
Estimate: 25 minutes
Actual: 23 minutes
"""
word_to_occurrence = {}
text = input("Text: ")
for word in text.split():
    try:
        word_to_occurrence[word] += 1
    except KeyError:
        word_to_occurrence[word] = 1

max_length = max(len(word) for word in list(word_to_occurrence.keys()))
for word, occurrences in sorted(word_to_occurrence.items()):
    print(f"{word:{max_length}}: {occurrences}")