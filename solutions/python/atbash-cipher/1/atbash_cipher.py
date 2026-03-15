import string

alphabet = string.ascii_lowercase
reverse_alphabet = alphabet[::-1]

# Create mapping dictionary
atbash = {a: b for a, b in zip(alphabet, reverse_alphabet)}

def encode(text):
    result = ""

    for char in text.lower():
        if char.isalpha():
            result += atbash[char]
        elif char.isdigit():
            result += char

    # group into 5 characters
    groups = [result[i:i+5] for i in range(0, len(result), 5)]
    return " ".join(groups)


def decode(text):
    result = ""

    for char in text.lower():
        if char.isalpha():
            result += atbash[char]
        elif char.isdigit():
            result += char

    return result