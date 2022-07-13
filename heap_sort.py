

def heapify(unsorted_list, n, i):

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and unsorted_list[largest] < unsorted_list[l]:
        largest = l
        
    if r < n and unsorted_list[largest] < unsorted_list[r]:
        largest = r
        
    if largest != i:
        unsorted_list[i], unsorted_list[largest] = unsorted_list[largest], unsorted_list[i]  # swap
  
        # Heapify the root.
        #print(unsorted_list)
        heapify(unsorted_list, n, largest)

def heap_sort(unsorted_list):
    
    n=len(unsorted_list)
    
    for i in range(n//2 - 1,-1,-1):
        heapify(unsorted_list, n, i)
        #print(unsorted_list)
        
    for i in range(n-1, 0, -1):
        unsorted_list[i], unsorted_list[0] = unsorted_list[0], unsorted_list[i]  # swap
        heapify(unsorted_list, i, 0)
        #print(unsorted_list)#'''




if __name__ == '__main__':
    unsorted_list = [0,99,5,4,3,2,1,6,8,9,7]
    heap_sort(unsorted_list)
    print(unsorted_list)