# 1
def countdown(num):
    return list(range(num, -1, -1)) 
print (countdown(5))
# 2
def print_and_return(lst):
    print(lst[0])
    return lst[1]
result = print_and_return([1, 2])
print(result)

#3

def plus_length(lst):
    return lst[0] + len(lst)
result = plus_length([1, 2, 3, 4, 5]) 
print(result)  
#4 
def values_greater_than_second(a):
    if len(a) < 2:
        return False
    
    b = a[1]
    new_list = [x for x in a if x > b]
    
    print(len(new_list))
    return new_list
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))
5#
def length_and_value(x, y):
    return [y] * x
print(length_and_value(4, 7)) 
print(length_and_value(6, 2))  