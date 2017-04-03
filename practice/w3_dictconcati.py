# dictionary concatination'

a = {1:2, 3:4,5:6}
b = { 10:16, 6:7, 8:9}
c = {}
for g in (a,b):c.update(g)
print(c)
