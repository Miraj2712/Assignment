def palindrome(string):
    return string == string[::-1]


String_input = input("Enter a string to check if it is a palindrome: ")
if palindrome(String_input):
    print(f"{String_input} is a palindrome.")
else:
    print(f"{String_input} is not a palindrome.")