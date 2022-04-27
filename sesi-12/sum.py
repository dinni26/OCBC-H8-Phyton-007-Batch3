def sum_self_made(list_of_numbers):
    '''to count sum of inputted list of numbers'''
    
    if(isinstance(list_of_numbers, tuple) or isinstance(list_of_numbers, list)):
        # sum = 1
        # sum = 2
        sum = 0
 
        for i in list_of_numbers: # [1, 2, 3]
            sum += i
   
        return sum
