
def partition(unsorted_list, low, high):
    
    pivot = unsorted_list[high]
    
    i = low-1
    
    for j in range(low, high):
        if unsorted_list[j] <= pivot:
            i= i+1
            
            unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
            
    unsorted_list[i+1], unsorted_list[high] = unsorted_list[high], unsorted_list[i+1]
    
    
    return i+1        
    
def quick_sort(unsorted_list, low, high):
    
    if low < high:
        
        pi = partition(unsorted_list, low, high)
        
        quick_sort(unsorted_list, low, pi-1)
        quick_sort(unsorted_list, pi+1, high)
        
        
        
    return unsorted_list   




if __name__ == '__main__':
    unsorted_list = [0,99,5,4,3,2,1,6,8,9,7]
    sorted_list = quick_sort(unsorted_list, 0, len(unsorted_list)-1)
    print(sorted_list)