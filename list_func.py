animals=["dog","cat","elephant",5,6,7]
number=[8,7,9,5,6,1]
print(type(animals))
copy=animals.copy() #copy the list


print(animals[1:4]) #slicing in list
print(animals[::-1]) #reverse the list by slicing

animals.append("lion") #added lion at the end of the list
animals.insert(5,"tiger") # added tiger at 5th index
animals.remove("dog") #remove the 1st dog string from the list
animals.extend(["cow","monkey",8,9]) #added another list 

poped=animals.pop()  #remove the last value of the list and store that index value
Index =animals.index(5) # store the index value of the string or integer
animals.reverse() #reverse the list
print(animals)
print(animals.count(5)) #print the how many times value occured




animals.clear()  #remove all the elements of list
print(Index)
print(poped)  # printed that last index value we stored
print(animals)  #print the list after all changes
print(copy)  # copy of the list where chnages not occured



#taking input from the user in list

list1= []  #make a empty list
l1 = int(input("Enetr the value:"))
list1.append(l1)
l2 = int(input("Enetr the value:"))
list1.append(l2)
l3 = int(input("Enetr the value:"))
list1.append(l3)
l4 = int(input("Enetr the value:"))
list1.append(l4)
l5 = int(input("Enetr the value:"))
list1.append(l5)
l6 = int(input("Enetr the value:"))
list1.append(l6)

print(list1)
list1.sort()
print(list1)
