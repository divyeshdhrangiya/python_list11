#how to declare list
a=[1,2,3,4,5,6]
print(a)



#list store multiple data in one list

b=[1,1.2,'hi','how']
print(b)



#list slicing
#list  start 0 posotion
c=[1,2,3,4,5,6]
print(c[2:])



#print reverce string

print(c[::-1])



#use methode in list

list1=[1,2,3,42,5]

#append data in list
list1.append(4)
print(list1)

#insert data specific position
list1.insert(1,11)
print(list1)


#last data remove in a list
list1.pop()
print(list1)


#specific data remove in a list give index
list1.pop(1)
print(list1)


#remove data into list

list1.remove(1)
print(list1)


#reverse print list
list1.reverse()
print(list1)

print(type(list1))