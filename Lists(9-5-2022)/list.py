#PYTHON LIST METHODS
#LIST IS A IMMUTABLE
#1.APPEND() METHOD
list=[1,2,3,4,5,"vaheeda","sameera"]
print("the list is:",list)
list.append(6)
print("the list after the append method:",list)
#EXTEND() METHOD
numbers=[7,8]
numbers.extend(list)
print("the list after the extend method is:",numbers)
#INSERT()
vowel=["a","e","o","u"]
vowel.insert(2,"i")
print("the list after the insert method is:",vowel)
#REMOVE() METHOD
prime_no=[2,3,5,7,9,11]
prime_no.remove(9)
print("the list after the remove method is:",prime_no)
#COUNT() METHOD
numbers=[2,3,4,5,6,6,6,6,6,7,8,9,10]
count=numbers.count(6)
print("count of 6 is:",count)
#POP() METHOD
prime_no=[2,3,5,7]
removed_ele=prime_no.pop(2)
print("removed element:",removed_ele)
print("the list after pop operation is:",prime_no)
#REVERSE() METHOD
prime_no.reverse()
print("the list after the reverse method is:",prime_no)
#SORT() METHOD
prime=[11,9,7,5,3,2]
prime.sort()
print("the list after the sort method is:",prime)
#COPY() METHOD
prime1=[2,3,5]
numbers=prime1.copy()
print("copied list:",numbers)
#CLEAR() METHOD
a=[1,2,3,4,5,6,7,8,9,10]
a.clear()
print("list after the clear():",a)#it prints the empty list
#SUM() METHOD
list2=[1,2,3,4,5,6,2,7,8,9,10]
a=sum(list2)
print("the sum of the list a is:",a)
#LENGTH() METHOD
print("the length of the list a is:",len(list2))
#INDEX METHOD
print("the index of the 2 is:",list2.index(2))
#MAX() METHOD
a=max(list2)
print("the maximum no of the list2 is:",a)
#MIN() METHOD
b=min(list2)
print("the minimum no of the list2 is:",b)
#pop() without index it remove the last element of the list
a=list2.pop()
print("the removed item is:",a)
print("the updated list will be:",list2)
#DEL() METHOD
del list2[6]
print("the list after del method will be:",list2)


