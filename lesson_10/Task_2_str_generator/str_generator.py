def word_gen(text: str):
    lst = text.split()
    for elem in lst:
        yield elem


for word in word_gen('i am generating words from text'):
    print(word)
