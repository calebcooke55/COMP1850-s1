
def calculate_travel_distance(tank_capacity, km_per_litre): 
    '''  
    This function calculates the distance a vehicle can travel based on tank  
    capacity (ie how many litres of fuel in tank) and the number of  
    kilometres a vehicle can travel per litre, and returns the  
    distance, rounded to two decimal points. 
    ''' 

    f_capacity = float(tank_capacity) 
    f_kml = float(km_per_litre) 
    distance = round(f_capacity * f_kml, 2) 
    return distance 

print(calculate_travel_distance(30.2, km_per_litre=3.3))

#a. It will work, as the function converts any input data type to a float
#b.i. No, as it cannot convert the enture thing into a float
#b.ii. Yes, as the value is already a float so does not need to be converted
#      into a float