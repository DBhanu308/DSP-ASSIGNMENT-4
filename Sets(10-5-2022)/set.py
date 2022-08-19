#SETS METHODS
#SET IS MUTABLE
#CREATING THE LIST
set={1,2,3,4,5,"vahii"}
print("the set is:",set)
print("the type of the set is:",type(set))
#ADD()
set.add("SUNNI")
print("the list after the add method:",set)
#DISCARD() METHOD REMOVING THE ELEMENTS WITH INDEX
set.discard(1)
print("the updated list will be:",set)
#REMOVE() METHOD
set.remove(5)
print("the set after the remove method will be:",set)
#POP() METHOD
set1={1,2,3,4,5,6,7,8,9,10}
set1.pop()
print("the set after the pop is:",set1)
#CLEAR() METHOD
set1.clear()
print("the set after the clear operation is:",set1)
#COPY() METHOD
set2=set.copy()
print("the set2 will be:",set2)
#DIFFERENCE() METHOD
a={10,20,30,40,80}
b={100,30,80,40,60}
print("the difference of(a-b):",a.difference(b))
print("the difference of(b-a):",b.difference(a))
#INTERSECTION() METHOD
print("the (a intersection b) is:",a.intersection(b))
print("the b intersection a is:",b.intersection(a))
#UNION() METHOD
print("the union of(aub):",a.union(b))
print("the union of(bua):",b.union(a))
#ISDISJOINT() METHOD
print("the isdisjoint method is:",a.isdisjoint(b))
print("the isdisjoint method is:",b.isdisjoint(a))
#ISSUBSET() METHOD
c={4,1,3,5}
d={6,0,4,1,5,0,3,5}
print("the issubset method is:",d.issubset(c))
print("the issubset method is:",c.issubset(d))
#ISSUPERSET() METHOD
print("the issuperset method:",c.issuperset(d))
print("the issuperset method:",d.issuperset(c))
#POP() REMOVE FORST ELEMENT FROM THE SET
s={"rem","rahim","ajay","rishav","aakash"}
print(s.pop())
print(s.pop())
print(s.pop())
print("updated set will be:",s)
#SYMMETRIC_DIFFERENCE METHOD
set1={1,2,3}
set2={2,3,4}
set3={3,4,5}
print("the symmetric_difference method is:",set1.symmetric_difference(set2))
print("the the symmetric_difference method is:",set2.symmetric_difference(set3))
#UPDATE METHOD
set2=[10,11,12]
set1={1,2,3}
print(set1.update(set2))

