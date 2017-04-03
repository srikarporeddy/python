'''#w3_length.py legth of the string

def string_length(str):
 count = [0]
 for char in str:
 	count += 1
 return count 
print(string_length('srikar'))

'''
def string_length(str):
	length = 0
	for char in str:
		length += 1
	return length
print(string_length(input('enter a value  : ')))

p = 'srikar'
print(len(p))
