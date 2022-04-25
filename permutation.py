#integer permutation with recursion
def function_permutation():
  input_array = input("Number of array: ").split() #split input string into array
  if(input_jumlah_array == 0): #if input_jumlah_array is 0
    print("") #print nothing
  else:
      for i in range(input_jumlah_array): #for i in range(input_jumlah_array)
          input_array[i] = int(input_array[i]) #convert string to integer
      def permutation(input_array, i = 0): #def permutation(input_array, i = 0)
          if(i == len(input_array)): #if i == len(input_array)
              print(" ".join(map(str, input_array))) #print input_array
          else:
              for j in range(i, len(input_array)): #for j in range(i, len(input_array))
                  input_array[i], input_array[j] = input_array[j], input_array[i] #swap input_array[i] and input_array[j]
                  permutation(input_array, i + 1) #call permutation(input_array, i + 1)
                  input_array[i], input_array[j] = input_array[j], input_array[i] #swap input_array[i] and input_array[j]
      permutation(input_array) #call permutation(input_array)

try:
  input_jumlah_array = int(input("Length of array: "))
  function_permutation()
except:
  print("That's not a number")