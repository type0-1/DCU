"""
Algorithms:

"""

# Linear Search:

# Time Complexity: O(n). Space Compelxity: O(1)

def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return f'{value} located at position {i}'
    return -1

# Bubble Sort:

# Time Complexity: O(n^2). Space Complexity O(1)
# Bubble Sorting from Largest to Smallest

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array



if __name__ == "__main__":
    array = [1, 5, 3, 7, 2]
    value = 5

    print(linear_search(array, value))
    print(bubble_sort(array))

