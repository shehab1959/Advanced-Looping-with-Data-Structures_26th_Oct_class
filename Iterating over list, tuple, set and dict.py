###Iterating over List, Tuple, Set and Dictionary

##Ordered collection (List)
fruit_list = ["Apple", "Banana", "Cherry", "Mango", "Guava"]
for i in fruit_list:
    print(f"Processing {i}") 
#Processing Apple
#Processing Banana
#Processing Cherry
#Processing Mango
#Processing Guava

print("Start Tuple:")
##Ordered collection (Tuple)
sports_list = ("Football", "Cricket", "Badminton")
for i in sports_list:
    print(f"Processing {i}") 
#Processing Football
#Processing Cricket
#Processing Badminton


print("Start Set:")
##Unordered Colletion (Set)
sports_list = {"Football", "Cricket", "Badminton"}
for i in sports_list:
    print(f"Processing {i}")
#Processing Badminton
#Processing Football
#Processing Cricket


print("Start Dict:")
##Dictionary
student = {
    "name" : "Shehab",
    "age" : 20,
    "city" : "Gazipur"
}

for i in student:
    print(i) #name,age,city

#or
for i in student.keys():
    print(i) ##name,age,city

for i in student.values():
    print(i) #Shehab,20,Gazipur

for i in student.items():
    print(i) #Output show on the list (packed obosthay)
#('name', 'Shehab')
#('age', 20)
#('city', 'Gazipur')


##if we want to see this output on Unpacked condition, then:
student = {
    "name" : "Shehab",
    "age" : 20,
    "city" : "Gazipur"
}
for i in student.items():
    key,values = i
    print(key,values) #Show output on unpack obosthay
#name Shehab
#age 20
#city Gazipur


print("Similar Alternative way:")
#or:
for key,values in student.items():
    print(key,values) #show same output as previous (Unpack obosthay)
#name Shehab
#age 20
#city Gazipur
