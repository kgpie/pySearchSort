

def merge_sort(unsorted_list):

    if len(unsorted_list)<=1:
        return unsorted_list
        
    
    mid = len(unsorted_list)//2
        
    left_array = unsorted_list[:mid]
    right_array = unsorted_list[mid:]
    
    left_array=merge_sort(left_array)
    right_array=merge_sort(right_array)
    return list(merge(left_array,right_array))
    
    
def merge(leftA,rightA):
    
    res=[]
    while len(leftA)!=0 and len(rightA)!=0:
        if leftA[0]< rightA[0]:
            res.append(leftA[0])
            leftA.remove(leftA[0])
        else:
             res.append(rightA[0])
             rightA.remove(rightA[0])
        
    if len(leftA)==0:
        res = res+rightA
    elif len(rightA)==0:
        res = res + leftA
        
    return res


if __name__ == '__main__':
    unsorted_list = [5,4,3,2,1,6,8,9,7,0]
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)