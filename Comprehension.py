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




##Example:05 (Using Dict)
price_list = {"rice":60, "oil":200, "sugar":100, "milk":92}
discounted_price_list = {}

for item,price in price_list.items():
    #discounted_price_list.update({item:price*0.9}) Use this, Or:
    discounted_price_list[item] = price*0.9 
print(discounted_price_list) #{'rice': 54.0, 'oil': 180.0, 'sugar': 90.0, 'milk': 82.8}


#Comprehension form given below:
price_list = {"rice":60, "oil":200, "sugar":100, "milk":92}
discounted_price_list = {item:price*0.9 for item,price in price_list.items()}
print(discounted_price_list) #{'rice': 54.0, 'oil': 180.0, 'sugar': 90.0, 'milk': 82.8}




##
price_list = {"Cha":15, "Biri":20, "Pan":12, "milk":22}
discounted_price_list = {}

for item,price in price_list.items():
    #discounted_price_list.update({item:price*0.9}) Use this, Or:
    discounted_price_list[item] = price*0.9 
print(f"Previous price was: {price_list}") #Previous price was: {'Cha': 15, 'Biri': 20, 'Pan': 12, 'milk': 22}
print(f"Now Updated Discount Price is: {discounted_price_list}") #Now Updated Discount Price is: {'Cha': 13.5, 'Biri': 18.0, 'Pan': 10.8, 'milk': 19.8}
