def first_word(text):
    text = text.strip('.,')
    words = text.split()
    first_word = words[0]
    if "`" in first_word:
        return first_word
    if first_word.isalpha():
        return first_word
    for word in words[1:]:
        if word.isalpha():
            return word
        if word.isalnum() and "`" in word:
            return word

print(first_word(input("Enter text :")))