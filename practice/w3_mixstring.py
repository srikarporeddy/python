# mix up two strings and genetrate new string

def mix_string(a,b):
	new_a = a[2:]+b[-2:]
	new_b = b[2:]+a[-2:]

	return new_a + '  ' + new_b

p = input(' enter a value ')
q = input ('enter b value')

print (mix_string( p , q))