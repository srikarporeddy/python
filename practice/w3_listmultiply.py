#w3_listmultiply.py
# multiply list with all other values

def multiply_list(items):
	tot = 1
	for x in items:
		tot *= x
	return tot
print(multiply_list([1,2,3,4,5]))