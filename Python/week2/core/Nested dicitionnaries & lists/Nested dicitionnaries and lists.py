#Update Values in Dictionaries and Lists
#1
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)

#2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']="Bryant"

print(students)




#3
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
#4

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)

#Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for dictionary in some_list:
        output = []
        for key, value in dictionary.items():
            output.append(f"{key} - {value}")
        print(", ".join(output))
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary(students)



