# 1) Countdown
def countdown(num):
    arr = []
    for x in range(num, -1, -1): # start = num, end = -1, decrement by 1
        arr.append(x) # add to the list
    return arr
x = countdown(5)
print(x)
#Log [5,4,3,2,1,0]

# 2) Print and Return
def print_and_return(arr):
    print(arr[0]) # access first list element
    return arr[1] # return the second element
x = print_and_return([1,2])
print(x)
# Log 1, Log 2

# 3) First Plus Length
def first_plus_length(arr):
    return arr[0] + len(arr) # return first value and length
sum = first_plus_length([1,2,3,4,5])
print(sum)
# Log 6

# 4) Values Greater than Second
def values_greater_than_second(arr):
    if(len(arr) < 2):
        return False
    else:
        returnArr = []
        total = 0
        for x in arr:
            if(arr[1] < x):
                total += 1
                returnArr.append(x)
        print(total)
        return returnArr
x = values_greater_than_second([5,2,3,2,1,4])
print(x)
# Log 3, Log [5,3,4]

# 5) This Length, That Value
def this_length_that_value(size, value):
    arr = []
    for x in range(0,size):
        arr.append(value)
    return arr
x = this_length_that_value(5, 3)
print(x)
# Log [3,3,3,3,3]