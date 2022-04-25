#integer powering with recursion
def powering(num,num2):
    if num2 == 0:
        return 1
    else:
        return num * powering(num,num2-1)
try:
  input_num = int(input("Bilangan X: "))
  input_num2 = int(input("Bilangan n pangkat: "))
  print(powering(input_num,input_num2))
except:
  print("That's not a number")