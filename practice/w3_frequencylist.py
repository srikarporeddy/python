import collections
my_list = [10 ,10, 10 , 10 , 20 ,20 ,20, 30, 40 ,50,20, 30, 40 ,50,20, 30, 40 ,50]
print("orginal list : ",my_list)
ctr = collections.Counter(my_list)
print("frequeny of the elements in the list : ", ctr)

my_list2 = input("Enter list values : ") #['q','q','q','s','s','e','e','f','g','g','r','r','r']
print("orginal list : ",my_list2)
ctr2 = collections.Counter(my_list2)
print("frequeny of the elements in the list : ", ctr2)







