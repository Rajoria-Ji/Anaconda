s = set()  #an empty set
print(type(s))



s={1,2,3,4,4,5,5,5,"happy"} 
u={-1,-2,-3}
c={2,3,4}
print(s)  #elements does not repeat in set, it is unordered



s.add("Sumit")  #add an element in a set
print(s)
s.update([7,8,6])   # add multiple elements in a set
s.remove("Sumit")    # remove a element from the list key error if not exist 
s.discard("Sumit")   # remove a specific element not rise error if not exist
p=s.pop()           # remove a random element
print(p)            # print a random element which stored in p by pop
print(s)
print(s.union(u))   # combine elements of both set without duplication
print(s.intersection(c))  # print the common elements of both set
print(s.difference(c))   #  print the elements which is not common in both set
print(c.issubset(s))    # checks is c is a subset of s or not 
print(u.isdisjoint(c))   #checks is c and u have not common elements or not

