

def insertion_sort(unsorted_list):
	
    for i in range(1, len(unsorted_list)):
        
        key = unsorted_list[i]
        
        j=i-1
        
        while key < unsorted_list[j] and j>=0:
            unsorted_list[j+1]=unsorted_list[j]
            j=j-1
        unsorted_list[j+1] = key
       
    return unsorted_list 
    
if __name__ == '__main__':
    unsorted_list = [5,4,3,2,1,6,8,9,7,0]
    sorted_list = insertion_sort(unsorted_list)
    print(sorted_list)
     