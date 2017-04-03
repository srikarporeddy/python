#w3_firatlast.py
# form a new string with first and last 2 elemens in the string

def str_from_both_ends(str):
	if len(str)< 2:
		return ''

	return str[0:2]+str[-2:]

print(str_from_both_ends(input('enter string value : \n')))




'''def new_object(obj):
	if len(obj)>2:
		print (obj[0:2]+obj[-2:](input('enter a string:')))


	else:
		print('done')	'''

		