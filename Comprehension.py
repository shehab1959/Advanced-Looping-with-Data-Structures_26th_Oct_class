###Comprehension

##Example:01
numbers = [2,5,7,9]
square_numbers = []
for i in numbers:
    square_numbers.append(i**2)
print(square_numbers) #[4, 25, 49, 81]


#Comprehension form given below:
numbers = [2,5,7,9]
square_numbers = [i**2 for i in numbers]
print(square_numbers) #[4, 25, 49, 81]



##Example:02
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