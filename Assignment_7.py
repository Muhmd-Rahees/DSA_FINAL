# Write a program to convert prefix expression to infix expression.

def is_operator(items):
    return items in {'+','-','*','/','^'}

def prefix_to_infix(pref_expression):
    stack = []
    operator = set(['+','-','*','/','^'])
    pref_expression = pref_expression[::-1]

    for items in pref_expression:
        if not is_operator(items):
            stack.append(items)
        else:
            opr1 = stack.pop()
            opr2 = stack.pop()
            infix_expression = '(' + opr1 + items + opr2 + ')'
            stack.append(infix_expression)
            return stack[0]
pref_expression = "+*AB-CD"
infix_expression = prefix_to_infix(pref_expression)
print( ("Prefix Expression: " , pref_expression))
print("Infix Expression : ",infix_expression)
       