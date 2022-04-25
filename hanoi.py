#tower of hanoi with recursion
import time

def hanoi(n, from_peg, to_peg, temp_peg):
    if n == 1: # base case
        print("Move disk 1 from peg", from_peg, "to peg", to_peg) # move disk from from_peg to to_peg
        return  # return from base case
    hanoi(n-1, from_peg, temp_peg, to_peg) # move n-1 disks from from_peg to temp_peg
    print("Move disk", n, "from peg", from_peg, "to peg", to_peg) # move nth disk from from_peg to to_peg
    hanoi(n-1, temp_peg, to_peg, from_peg) # move n-1 disks from temp_peg to to_peg

try:
  n = int(input("Enter number of disks: ")) # get number of disks
  start = time.time() # start timer
  hanoi(n, 'source', 'target', 'helper') # call hanoi function
  end = time.time() # end timer
  print("Total time:", end - start) # print total time
  #count steps to move n disks from source to target
  print("Total steps:", 2**n - 1) # print total steps
except:
  print("That's not a number")
