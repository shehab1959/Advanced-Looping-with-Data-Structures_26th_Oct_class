###enumerate()

fruit_list = ["Apple","Banana","Cherry","Mango"]
for i in fruit_list:
    print(i) #Apple,Banana,Cherry,Mango (only elements, without index number)
print(len(fruit_list)) #4
print(list(range(len(fruit_list)))) #[0, 1, 2, 3]

#using enumerate() (printing elements with natural index number)
fruit_list = ["Apple","Banana","Cherry","Mango"]
for idx,item in enumerate(fruit_list):
    print(idx,item)
#0 Apple
#1 Banana
#2 Cherry
#3 Mango


#start from 15
sports_list = ["Football","Cricket","Badminton"," Vollyball"]
for i,j in enumerate(sports_list, start = 15):  #here i means index number, j means item/element
    print(i,j)
#15 Football
#16 Cricket
#17 Badminton
#18  Vollyball



###Zip()

user_id = ["001","002","003","004"] #4
user_name = ["Alvi","Sadia","Abir","Mollah"] #4
user_age = [20,22,23,27] #4
user_email = ["alvi230@diu.du.bd","sadia231@diu.du.bd","abir231510@diu.du.bd","mollah4200@diu.du.bd"] #4

for idx in range(len(user_id)):
    print(user_id[idx],user_name[idx],user_age[idx],user_email[idx])
#001 Alvi 20 alvi230@diu.du.bd
#002 Sadia 22 sadia231@diu.du.bd
#003 Abir 23 abir231510@diu.du.bd
#004 Mollah 27 mollah4200@diu.du.bd


#using list
print(list(zip(user_id,user_name,user_age,user_email)))
#[('001', 'Alvi', 20, 'alvi230@diu.du.bd'), ('002', 'Sadia', 22, 'sadia231@diu.du.bd'), ('003', 'Abir', 23, 'abir231510@diu.du.bd'), ('004', 'Mollah', 27, 'mollah4200@diu.du.bd')]


#Using zip()
for i in zip(user_id,user_name,user_age,user_email):
    print(i)
#('001', 'Alvi', 20, 'alvi230@diu.du.bd')
#('002', 'Sadia', 22, 'sadia231@diu.du.bd')
#('003', 'Abir', 23, 'abir231510@diu.du.bd')
#('004', 'Mollah', 27, 'mollah4200@diu.du.bd')


#another example
user_id = ["001","002","003","004","005"] #5
user_name = ["Alvi","Sadia","Abir","Mollah"] #4
user_age = [20,27] #2
user_email = ["alvi230@diu.du.bd","sadia231@diu.du.bd","abir231510@diu.du.bd","mollah4200@diu.du.bd"] #4

for i in zip(user_id,user_name,user_age,user_email):
    print(i)
#Output show only two element as lowest 2, there is no same number of element of each class
#('001', 'Alvi', 20, 'alvi230@diu.du.bd')
#('002', 'Sadia', 27, 'sadia231@diu.du.bd')