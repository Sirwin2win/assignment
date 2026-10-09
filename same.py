text = 'This is a good place to be, in the presence of God. To enjoy him and be the best'
def word_frequency(text):
    text = text.lower()
    text = text.replace(",", "")
    words = text.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts
frequencies = word_frequency(text)
print(frequencies)

