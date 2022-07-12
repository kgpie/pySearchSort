

def selection_sort(input_list):
    
    for i in range(len(input_list)):
    
        min_idx = i
            
        for j in range(i+1,len(input_list)):
            
            if input_list[j]<input_list[min_idx]:
                min_idx = j
                
        input_list[i],input_list[min_idx]=input_list[min_idx],input_list[i]
        
    return input_list


if __name__ == '__main__':
    unsorted_list = [5,4,3,2,1,6,8,9,7,0]
    sorted_list = selection_sort(unsorted_list)
    print(sorted_list)
     