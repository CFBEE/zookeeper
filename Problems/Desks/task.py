class1 = int(input())
class2 = int(input())
class3 = int(input())

desks = (class1 // 2 + class1 % 2) + (class2 // 2 + class2 % 2) + \
        (class3 // 2 + class3 % 2)
print(desks)
