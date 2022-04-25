#integer print down with recursion
def print_down(num):
    if num == 0:
        print(num)
    else:
        print(num)
        print_down(num-1)
try:
  input_num = int(input("Enter a number: "))
  print_down(input_num)
except:
  print("That's not a number")