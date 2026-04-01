def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    # convert sentence to lowercase and get only letters
    letters = set(sentence.lower())

    return alphabet <= letters