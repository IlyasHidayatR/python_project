#reverse string with recursion
input_str = input("Enter a string: ")
def reverse_str(str):
    if len(str) == 0:
        return ""
    else:
        return reverse_str(str[1:]) + str[0]
print(reverse_str(input_str))