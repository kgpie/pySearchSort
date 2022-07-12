

def bubble_sort(input_list):
	
    
    for i in range(1,len(input_list)):
        
        for j in range(i):
            
            if input_list[i]<input_list[j]:
                input_list[j],input_list[i]  = input_list[i], input_list[j]
                
            
    return input_list
    
 
if __name__ == '__main__':
    unsorted_list = [5,4,3,2,1,6,8,9,7,0]
    sorted_list = bubble_sort(unsorted_list)
    print(sorted_list)