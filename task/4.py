def invert_string(input_str):
    return input_str[::-1]

orginal_string = "hello world"
inverted_string = invert_string(orginal_string)
print(inverted_string) # dlrow olleh


def is_palindrome(input_str):
    return invert_string(input_str) == input_str

test1 = "abra"
print(is_palindrome(test1)) # False
test2 = "abrarba"
print(is_palindrome(test2)) # True
