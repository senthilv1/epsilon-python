a= [2, 3, 5, -4, -2, -6]


#map:
print (list(map(lambda x:x**2 , a)))

#filter :
b=[]
for i in range(0,len(a)):
    if a[i] > 0:
        b.append(a[i])
        
print(b)

print (list(filter(lambda x:x>0, a)))

