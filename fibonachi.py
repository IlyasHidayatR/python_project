#fibonachi with recursion
def fibonachi(num):
    if num == 0: #base case
        return 0 
    elif num == 1: #base case
        return 1
    else:
        return fibonachi(num-1) + fibonachi(num-2) #recursion
try:
  input_num = int(input("Enter a number: "))
  print(fibonachi(input_num)) #call function
except:
  print("That's not a number")