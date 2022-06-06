
class Lst1GtLst2(Exception):
    pass

class Lst2GtLst1(Exception):
    pass

class Lst1NELst2(Exception):
    pass

l1 = [1, 2, 3]
l2 = [1, 2, 3]

try:
    if l1 > l2:
        raise Lst1GtLst2("List1 values are greater than list2 values")
    elif l2 > l1:
        raise Lst2GtLst1("List2 values are greater than list1 values")
    elif l1 != l2:
        raise Lst1NELst2("List2 values are not equal to list1 values")

except Lst1GtLst2 as g:
    print(g)
except Lst2GtLst1 as l:
    print(l)
except Lst1NELst2 as e:
    print(e)
except Exception as x:
    print(x)
else:
        print(f"Both lists are equal: \nl1 :{l1}\nl2 :{l2}")

finally:
        print("comparison of lists completed......")