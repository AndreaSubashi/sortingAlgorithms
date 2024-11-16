import sys

# 2.1 Sort Checking
def isSorted(arr):
    """
    Check if an array is sorted in ascending order.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False,arr
    return True,arr

# 2.2 Inversion Count
def countInversions(arr):
    """
    Count the number of inversions in an array.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    Worst case: Number of inversions is sumation of all integers until (n-1)
    """
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

# 2.3 Mergesort
def mergeSort(arr):
    """
    Implement the fully recursive version of mergesort.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    comparisons = 0

    def merge(left, right):
        nonlocal comparisons
        merged = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        #Append the remaining elements of left and right arrays
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    def mergeSortHelper(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = mergeSortHelper(arr[:mid]) #sort the left half of the array
        right = mergeSortHelper(arr[mid:]) #sort the right half of the array

        return merge(left, right)

    arr = mergeSortHelper(arr)
    return comparisons, arr

# 2.4 Heapsort
#---max heap---
def heapSort(arr):
    """
    Implement the heapsort algorithm.
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    comparisons = 0

    #maintains max heap order
    def heapify(arr, n, i):
        nonlocal comparisons
        largest = i
        #standard formula for index in binary heap
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            comparisons += 1
            if arr[largest] < arr[left]:
                largest = left

        if right < n:
            comparisons += 1
            if arr[largest] < arr[right]:
                largest = right
                
        #check if idx of largest != to idx of root node in subtree
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # Build max heap
    #n//2-1 -> last none leaf node formula
    #iterates from last non-leaf node to the root and heapifies in the process,
    #we dont't include the leaf nodes since they have no children and heapify 
    #works by comparing parents to children
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap current max element with element in index [i]
        heapify(arr, i, 0) # Heapify to max heap order, since order was violated by swap

    return comparisons, arr

# 2.5 Quicksort
def quickSort(arr):
    """
    Implement the quicksort algorithm with an in-place partition and
    a pivot selection strategy that avoids O(n^2) time complexity.
    Time Complexity: O(n log n) (average case)
    Space Complexity: O(log n) (for recursive calls)
    """
    comparisons = 0

    def partition(arr, low, high):
        nonlocal comparisons
        # Choose the pivot as the median of the first, middle, and last elements: this avoids worst case scenario
        pivot_indices = [low, (low + high) // 2, high]
        #create list using values of idx of pivot_indices
        pivot_values = [arr[i] for i in pivot_indices]
        pivot_values.sort()
        #find median index of pivot_indices
        pivot_index = pivot_indices[pivot_values.index(arr[(low + high) // 2])]
        #assign pivot as value of pivot_index
        pivot = arr[pivot_index]

        # Move the pivot to the end
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        # Use Lomuto partition scheme
        i = low
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        return i

    #d&q
    def quickSortHelper(arr, low, high):
        nonlocal comparisons
        #if at least 2 elementts
        if low < high:
            pivot_index = partition(arr, low, high)
            quickSortHelper(arr, low, pivot_index - 1)
            quickSortHelper(arr, pivot_index + 1, high)

    quickSortHelper(arr, 0, len(arr) - 1)
    return comparisons, arr

# 2.6 Ins-Mergesort
def insMergeSort(arr, M):
    """
    Implement the Ins-Mergesort algorithm with a parameter M.
    Time Complexity: O(n log n) (if M is chosen appropriately)
    Space Complexity: O(n)
    The main issue is to decide the value of M. Insertion sort
    is better if data is already nearly sorted (since it skips over it)
    or in smaller data sets. Mergesort performs better on large data sets.
    """
    comparisons = 0

    #mergesort code
    def merge(left, right):
        nonlocal comparisons
        merged = []
        i, j = 0, 0
        
        if left is None:
            return right
        if right is None:
            return left
        
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    def insMergeSortHelper(arr):
        nonlocal comparisons
        n = len(arr)
        
        if n <= M:
            #for clarification
            
            # Use insertion sort for small arrays
            for i in range(1, n):
                key = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > key:
                    comparisons += 1
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
                
            return arr
            

        mid = n // 2
        left = insMergeSortHelper(arr[:mid])
        right = insMergeSortHelper(arr[mid:])

        return merge(left, right)  # Merge the two sorted halves

    sorted_arr = insMergeSortHelper(arr)
    return comparisons, sorted_arr



#---------------------------------------------------------------------------------------------------

def readInput(filename):
    """ Read the input array from a text file.
    The file should have the following format:
    First line: n (size of the array)
    Second line: n comma-space separated non-negative 32-bit integer values
    """
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        if n == 0: 
            arr = []
        else:
            """
            line reads the second line of the file, strips any leading or trailing whitespace,
            splits it by commas followed by spaces, and converts each element to an integer. 
            """
            arr = [int(x) for x in file.readline().strip().split(', ')]
            if len(arr) != n:
                raise ValueError("Invalid input file format")
    return arr

def main(algorithm, filename):
    """ Run the specified sorting algorithm on the input array from the file. """
    arr = readInput(filename)
    if algorithm == 'issorted':
        result = isSorted(arr)
        print(f"Is the array sorted? {result}")
    elif algorithm == 'countinversions':
        inversions = countInversions(arr)
        print(f"Number of inversions: {inversions}")
    else:
        if algorithm == 'mergesort':
            comparisons = mergeSort(arr.copy())
        elif algorithm == 'heapsort':
            comparisons = heapSort(arr.copy())
        elif algorithm == 'quicksort':
            comparisons = quickSort(arr.copy())
        elif algorithm == 'insmergesort':
            M = 7  #Best overall value for M after testing
            comparisons = insMergeSort(arr.copy(), M)
        else:
            print(f"Invalid algorithm: {algorithm}")
            return
        print(f"Number of comparisons and ordered list: {comparisons}")

"""
def test_insMergeSort(N):
    
    Used for generating the values of M for each group of |n|
    Test different values of M for array sizes from 1 to N with random arrays.
    
    results = []
    for n in range(0, N + 1, 10):
        for m in range(1, n):
            arr = [random.randint(0, 1000) for _ in range(n)]  # Generate random array of size n
            comparisons = insMergeSort(arr, m)
            results.append((m, n, comparisons))

    return results


# Example usage
N = 500 # Test for array sizes from 1 to N
results = test_insMergeSort(N)
def save_results_to_file(results, filename):
    
    Save the results to a file.
    
    with open(filename, 'w') as file:
        for result in results:
            file.write(f"M: {result[0]}, N: {result[1]}, Comparisons: {result[2]}\n")


# Example usage
N = 500  # Test for array sizes from 1 to N
results = test_insMergeSort(N)
save_results_to_file(results, 'test_im_results.txt')
"""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sorting.py <algorithm> <input_file>")
        sys.exit(1)
    #argument 1 = to alg name lowecase    
    algorithm = sys.argv[1].lower()
    #argumanr 2 = file of input
    filename = sys.argv[2]
    main(algorithm, filename)
    
    
