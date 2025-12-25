def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    result = ''.join(reversed_words)
    return result
    # return " ".join(word[::-1] for word in sentence.split())
print(reverse_words("Hello World"))
print(reverse_words("Python is fun!"))
print(reverse_words("This is a  test   with   multiple spaces"))
print(reverse_words("s'teL    ecitcarp"))