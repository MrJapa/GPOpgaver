import bisect
#.
#.Opgave 1
def Interchange():
    x = 5
    y = 10
    print(x,y)

    z = x
    x = y
    y = z
    print(x,y)
#.Opgave 2
def InterchangeTriple():
    x = 5
    y = 10
    z = 15
    print(x,y,z)
    
    temp = z
    z = x
    x = y
    y = temp
    print(z,x,y)
#.Opgave 3
def isPalindrome(s):
        return s == s[::-1]
def driver():
    s = "maoam"
    ans = isPalindrome(s)
    if ans:
        print("Yes")
    else:
        print("No")
#.Opgave 4
def StepsInLinearSearch():
    l = [1,3,4,5,6,8,9,11]
    length = len(l)
    for i in range(length):
        print(l[i])
        if i == 9:
            break
#.Opgave 5
def InsertSortedList():
    l = [1,3,6,9,12,16,22]
    bisect.insort(l,10)
    print(l)
#.Opgave 6
def ArrayOfMultiples():
    x = 5
    y = 10
    num_range = range(x,y+1)
    num_list = list(num_range)
    print(num_list)
#.Opgave 7
def PowerRanger():
    Count = 0
    n = 3
    min = 6
    max = 1000
    for i in range(max):
        if i**n in range(min,max):
            print('{}^{} Lies Between {} And {}'.format(i,n,min,max))
            Count += 1
    print('Total Values Found =',Count)

