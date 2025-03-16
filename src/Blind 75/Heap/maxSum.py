def maxSum(grid, limits, k):
    """
    :type grid: List[List[int]]
    :type limits: List[int]
    :type k: int
    :rtype: int
    """
    maxVals = []
    def maxHeapify(arr, i, end):
        if i == end:
            return
        n = len(arr)
        l = 2*i+1  # Left child
        r = 2*i+2  # Right child
        
        # Find largest among root, left child and right child
        largest = i
        
        if l < n and arr[l] > arr[largest]:
            largest = l
        
        if r < n and arr[r] > arr[largest]:
            largest = r
        
        # Swap and continue heapifying if root is not largest
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            maxHeapify(arr, largest, end)
    
    def buildMaxHeap(arr, end):
        for i in range(end-1, -1, -1):
            maxHeapify(arr, i, end)

    def heapsort(arr, end, targetArr):
        buildMaxHeap(arr, end)
        for i in range(end-1, -1, -1):  # Fix range to work with end parameter
            # Swap root with last element
            temp = arr[0]
            arr[0] = arr[i]
            arr[i] = temp
            targetArr.append(temp)
            
            # Reduce heap size and heapify the root
            maxHeapify(arr, 0, i-1)  # Fix end parameter - use i not i-1

    for i in range(len(limits)):
        heapsort(grid[i], limits[i], maxVals)

    
    
    res = 0
    maxVals.sort(reverse=True)
    for i in range(k):
        res += maxVals[i]

    return res


# print(maxSum([[1,2],[3,4]], [1,2], 2)) #7
# print(maxSum([[5,3,7],[8,2,6]], [2,2], 3)) #21


def maxSum2(grid, limits, k):

    maxVals = []
    def maxHeapify(arr, i, heapSize):
        l = 2*i + 1  # leftNode(i)
        r = 2*i + 2  # rightNode(i)
        
        # Find the largest among node i and its children
        largest = i
        
        # Check if left child exists and is greater than current largest
        if l < heapSize and arr[l] > arr[i]:
            largest = l
        else:
            largest = i
            
        # Check if right child exists and is greater than current largest
        if r < heapSize and arr[r] > arr[largest]:
            largest = r
        
        # If largest is not the current node, swap and recursively heapify
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            maxHeapify(arr, largest, heapSize)

    def buildMaxHeap(arr, size):
        # Start from the last non-leaf node and go up to the root
        for i in range(size//2, -1, -1):
            maxHeapify(arr, i, size)

    def heapSort(arr, k, targetArr=None):
        if targetArr is None:
            targetArr = []
    
        n = len(arr)
        
        # If k is greater than array length, sort the whole array
        k = min(k, n)
        
        # Build max heap
        buildMaxHeap(arr, n)
        
        # Extract only k elements
        heapSize = n
        for i in range(k):
            if heapSize <= 0:
                break
                
            # Move current root (maximum) to the end of the considered portion
            arr[0], arr[heapSize-1] = arr[heapSize-1], arr[0]
            
            # Store the maximum value in targetArr if provided
            if targetArr is not None:
                targetArr.append(arr[heapSize-1])
            
            # Reduce heap size and heapify the root
            heapSize -= 1
            maxHeapify(arr, 0, heapSize)

    
    for i in range(len(limits)):
        heapSort(grid[i], limits[i], maxVals)

    
    
    res = 0
    maxVals.sort(reverse=True)
    for i in range(k):
        res += maxVals[i]

    return res

print(maxSum2([[1,2],[3,4]], [1,2], 2)) #7
print(maxSum2([[5,3,7],[8,2,6]], [2,2], 3)) #21