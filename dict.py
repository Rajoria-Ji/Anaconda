#it is unordered
# it is mutable
# it is indexed
# can not contain duplicate keys.


d={}      #an empty dictionary 

print(type(d)) 

dic = {1:'A',
       2:'B',
       3:'C',
       "List":[1,2,3],
       }


print(dic) #it will print the keys and values of dictionary
print(dic[1]) #it will print value of key 1
print(dic.items()) #it will print all keys and their
print(dic.keys()) #it will print all keys
print(dic.values()) #it will print all values
c=dic.copy() # it will store the copy of dictionary
dic.update({4:'D',5:'E'}) #it will add this key and value at the end of dictionary
print(dic.get(6)) #prints None


a=dic.pop(5) #remove that key from the dictionary
print(a)      #prints value of that removed key
b=dic.popitem() #remove the last key from the dictionary
print(b)    #returns the last key value pair
print(c)    #it will paste the copied dictionary 
print(len(dic))     # it will print the lenth of the dictionary 
print(dic.setdefault(6)) #prints a value of key, None if not found
#print(dic[6])     #Returns an error
# dic.clear()  #remove all items from the dictionary