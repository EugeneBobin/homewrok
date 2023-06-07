def popular_words(text, words):
    text = text.lower()
    word_count = {word: 0 for word in words}

    for word in text.split():
        if word in word_count:
            word_count[word] += 1

    return word_count
print(popular_words(input("Enter the text :"), input("Enter the words :").lower().split(" ")))