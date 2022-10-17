import string
from collections import Counter


def find_words_with_repeated_letters(input_filename: str) -> list:
    with open(input_filename) as f:

        words = f.read().split()

    words_without_marks = []
    for word in words:
        for letter in word:
            if letter in string.punctuation:
                word = word.replace(letter, "")
        words_without_marks.append(word)

    words_that_duplicates = [i for i in words_without_marks if words_without_marks.count(i) > 1]

    letters_that_duplicate_in_duplicate_word = []
    for word in words_that_duplicates:
        for key, val in Counter(word).items():
            if val > 1:
                letters_that_duplicate_in_duplicate_word.append(word.lower())

    letters_that_duplicate_in_duplicate_word = list(set(letters_that_duplicate_in_duplicate_word))
    return letters_that_duplicate_in_duplicate_word


find_words_with_repeated_letters("input_words.txt")
print(find_words_with_repeated_letters("input_words.txt"))