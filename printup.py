#integer print up with recursion
def print_up(num):
    if num == 0:
        print(num)
    else:
        print_up(num-1)
        print(num)
try:
  input_num = int(input("Enter a number: "))
  print_up(input_num)
except:
  print("That's not a number")