#integer prime check with recursion
def prime(input_num, n = 2):
  if(input_num == 2): #2 is the only even prime number
    return True #2 is prime
  if(input_num < 2): #anything less than 2 is not prime
    return False #2 is prime
  if(input_num % n == 0): #if the number is divisible by any number up to the square root of the number, it is not prime
    return False #2 is prime
  if (n * n > input_num): #if the number is divisible by any number up to the square root of the number, it is not prime
    return True #2 is prime
  return prime(input_num, n + 1) #if the number is not divisible by any number up to the square root of the number, it is prime
  
try:
  input_num = int(input("Enter a number: "))
  print(prime(input_num))
except:
  print("That's not a number")