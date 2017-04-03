# replace repeated alphabet with $ 

def change_char(str1):
	char = str1[0]
	length = len(str1)
	str1 = str1.replace(char,'$')
	str1 = char + str1[1:]

	return str1
print(change_char(input('enter string value:  \n ')))

def change_char(str1):
	char = str1[0]
  	length = len(str1)
  	str1 = str1.replace(char, '$')
  	str1 = char + str1[1:]

  return str1

print(change_char(input('enter string value:  \n ')))



