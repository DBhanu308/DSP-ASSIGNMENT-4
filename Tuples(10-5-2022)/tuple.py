#TUPLE METHODS
#TUPLES ARE IMMUTABLE
#1.COUNT() METHOD
tuple1=(1,2,3,4,5,6)
print("the given tuple is:",tuple1)
print("the type of tuple1 is:",type(tuple1))
a=tuple1.count(2)
print("the count of 2 is:",a)
#INDEX() METHOD
b=tuple1.index(2)
print("the index of the 2 is:",b)
#PRINTING THE ELEMENTS OF THE TUPLE
for i in tuple1:
    print(i)

