# Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression

def postfix_to_prefix(postfix_expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for i in postfix_expression:
        if i not in operators:
            stack.append(i)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_expression = i + operand1 + operand2
            stack.append(prefix_expression)

    return stack[0]


postfix_expression = "34+"
prefix_expression = postfix_to_prefix(postfix_expression)
print("Postfix expression:", postfix_expression)
print("Prefix expression:", prefix_expression)

