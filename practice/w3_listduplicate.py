#finding duplicaes in the list 

a =  [10,20,30,20,10,50,60,40,80,50,40]  

dup_items = set()
uniq_ites = []

for x in a:
	if x not in dup_items:
		uniq_ites.append(x)
		dup_items.add(x)
print(dup_items)


l = []
if not l:
	print("list is empty")