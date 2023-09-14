# In[]:
# 1.	Given an array of consecutive integers. Create a function that counts the sum of all elements inside the array within O(1) time. 
# Sample array: 
# arrayInteger = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# Output: 
# 55

arrayInteger = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_of_consecutive_array(array):
    n = len(array)
    firstTerm = array[0]
    lastTerm = array[n-1]
    sum = (n/2) * (firstTerm + lastTerm)
    return int(sum)

print(sum_of_consecutive_array(arrayInteger))

# In[]:
# 2.	Given an array of integers (sorted). Create a function that returns the index of a specific element within O(log(n)) time. 
# Sample array: 
# arrayInteger = [10, 23, 45, 92, 101, 102, 103, 10001] 
# Input: 
# 102 
# Output: 
# 

arrayInteger = [10, 23, 45, 92, 101, 102, 103, 10001]
def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search(arrayInteger, 10))

# In[]:
# 3.	Given an array of integers (unsorted). Create a function that counts the number of occurrences of each element in the array. 
# Sample array: 
# arrayInteger = [5, 100, 12, 4, 5, 2, 12, 13] 
# Output: 
# 5 2x 
# 100 1x 
# 12 2x 
# 4 1x 
# 2 1x 
# 13 1x

arrayInteger = [5, 100, 12, 4, 5, 2, 12, 13]
def count_occurences(array):
    dict = {}
    for i in range(len(array)):
        if array[i] not in dict:
            dict[array[i]] = 1 
        else:
            dict[array[i]] += 1
    
    for key, value in dict.items():
        print(key, value, "x")

count_occurences(arrayInteger)

