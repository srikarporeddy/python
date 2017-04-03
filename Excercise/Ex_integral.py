# program will form a dictonary by taking input input valuew

n = int(input("Enter the number : "))

d=dict()
for i in range(1,n+1):
	d[i]=i*i
print(d)