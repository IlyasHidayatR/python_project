#integer multiplication with recursion
def multiplication(num,num2):
    if num2 == 0:
        return 0
    else:
        return num + multiplication(num,num2-1) #return num + multiplication(num,num2-1)
try:
  input_num = int(input("Enter a number: "))
  input_num2 = int(input("Enter another number: "))
  print(multiplication(input_num,input_num2))
except:
  print("That's not a number")