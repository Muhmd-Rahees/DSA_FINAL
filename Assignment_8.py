# Write a program to check if all the brackets are closed in a given code snippet.

def are_brackets_closed(code):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in code:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False

    return len(stack) == 0

code_snippet = "{(a + b) * [c - d]}"
if are_brackets_closed(code_snippet):
    print("All brackets are closed.")
else:
    print("Brackets are not properly closed.")
