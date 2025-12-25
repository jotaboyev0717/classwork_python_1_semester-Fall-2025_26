def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expression:
        if ch in "([{":
            stack.append(ch)

        elif ch in ")]}":
            if not stack:
                return False
            if stack.pop() != pairs[ch]:
                return False

        else:
            continue

    return len(stack) == 0


print(is_balanced("{[()]}"))          # True
print(is_balanced("{[}]"))            # False
print(is_balanced("(]"))              # False
print(is_balanced("((()))"))          # True
print(is_balanced("print(list[0])"))  # True
print(is_balanced("((("))             # False
print(is_balanced("]"))               # False

