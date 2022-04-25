#polynomial interpolation linear time O(n)
def interpolation_search(array, value):
    low = 0 # start at the beginning of the array
    high = len(array) - 1 # end at the end of the array
    while low <= high and value >= array[low] and value <= array[high]: # while the value is between the low and high index
        mid = low + int(((float(high - low) / (array[high] - array[low])) * (value - array[low]))) # calculate the mid index
        if array[mid] == value: # if the value is equal to the mid index
            return mid # return the mid index
        elif array[mid] < value: # if the value is less than the mid index
            low = mid + 1 # set the low index to the mid index plus 1
        else:
            high = mid - 1 # set the high index to the mid index minus 1
    return -1 # return -1 if the value is not found


print(interpolation_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
