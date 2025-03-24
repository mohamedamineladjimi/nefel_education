#1 countdown: 
def countdown (num):
    output = []
    for i in range(num,-1,-1):
        output.append(i)
    return output
print(countdown(5))


#2
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))
 
 #3
 def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))