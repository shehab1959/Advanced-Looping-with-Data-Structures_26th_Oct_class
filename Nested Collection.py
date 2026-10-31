d = [1,2,["hello","world"],True, {30,40,22},{"age":30},"Bangladesh",(22,34)]
d1 = d[5]
print(d1) #{'age': 30}
d2 = d[5]["age"]
print(d2) #30


##
L = [1,3,("red","green","BLUE"),True,"name",{"Alvi":2535, "Sadia":3565},[{"Apple":"Red","Guava":"Green"},57]]

#What is the colour of Guava?
L1 = L[6][0]["Guava"]
print(L1) #Green

print(L[-1]) #[{'Apple': 'Red', 'Guava': 'Green'}, 57]