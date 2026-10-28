
def func_1(lst_value): 
    ''' 
    This function takes a list of floats,
    and returns the average of all the values in
    the list
    ''' 
    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value

#A meaningful name for func_1() might be average_calc() as it
#calculates the average out of all the numbers

