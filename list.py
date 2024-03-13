#lists
#we can change the data inside the list
#square bracket
list1=["apple","banana","cherry","orange"]
print(list1)
print()

print(type(list1))
print()

for x in list1:
    print(x)
print()

list1[2]="watermelon"
print(list1)
print()

print(len(list1))
print()

print(list1.pop())
print(list1)
print()

list1.insert(1,"stawberry")
print(list1)
