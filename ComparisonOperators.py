def find_largest(numbers):
    largest = numbers[0]

    for num in numbers[1:]:
        if num > largest:
            largest = num
    
    return largest

def find_smallest(numbers):
    smallest = numbers[0]

    for num in numbers[1:]:
        if num < smallest:
            smallest = num
    
    return smallest

numbers = [5, 3, 7, 9, 2, 1]

print("The largest number in the array is: ", find_largest(numbers))
print("The smallest number in the array is: ", find_smallest(numbers))

