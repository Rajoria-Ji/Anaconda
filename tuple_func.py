t=() # a empty tuple
k=(5,) # a single value stored tuple
print(type(t))

#methods of tuple
t1=(1,2,3,4.5,4,9)

print(t1.count(4))  #count the how many times that value occured
print(t1.index(4))  #print first index value 


#function

print(min(t1))  #print the minimum value from the tuple
print(max(t1))  #print the maximum value from the tple
print(len(t1))  #print the how many values are thier
print(sum(t1)) #print the sum of the values if they are integer of float

#convert list into tuple
lis=[1,0,2,5]
t2=tuple(lis)

print(type(t2))
print(t2)

#packing & unpacking
t=4,5,6  #packing
a,b,c=t  #unpacking
print(a,b,c)


#nested tuples
tup= ((1,2),(3,4),(5,6)) #-->    0 1-----coloumn number
                               # 1 2 ---- row0
                               # 3 4 ---- row1
                               # 5 6 ---- row2
print(tup[2][1])