def is_palindrome(text):
    cleaned_text = ''
    for char in text:
        if 'a' <= char <= 'z':
            cleaned_text += char.lower
    reversed_text = cleaned_text[::-1]
    return cleaned_text == reversed_text 