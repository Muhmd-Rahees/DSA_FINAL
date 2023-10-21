# Write a recursive function to check if a given string is a palindrome.

def is_palindrome(string):

    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


input_string = input("Enter the characters")


if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
