###Comprehension

##Example:01 (Using list)
numbers = [2,5,7,9]
square_numbers = []
for i in numbers:
    square_numbers.append(i**2)
print(square_numbers) #[4, 25, 49, 81]


#Comprehension form given below:
numbers = [2,5,7,9]
square_numbers = [i**2 for i in numbers]
print(square_numbers) #[4, 25, 49, 81]



##Example:02 (Using list)
num = [2,5,7,9,10,12,13]
even_num = []
for i in num:
    if i % 2 == 0:
        even_num.append(i**2)
print(even_num) #[4, 100, 144]


#Comprehension form given below:
num = [2,5,7,9,10,12,13]
even_num = [i**2 for i in num if i % 2 == 0]
print(even_num) #[4, 100, 144]

"""
##Example:03 (Using Tuple)
num = tuple(range(1,20))
odd_num = ()
for i in num:
    if i%2 == 1:
        odd_num.append(i)
print(odd_num) #Error, as Tuple doesn't accept any add/change anything. So we don't need to comprehension it.
"""



##Example:04 (Using Set)
my_set = {1,7,9,7,3,9}
cube_of_even_numbers = set()

for i in my_set:
    cube_of_even_numbers.add(i**3)

print(cube_of_even_numbers) #{1, 27, 729, 343} Here remove duplicaate number cube

