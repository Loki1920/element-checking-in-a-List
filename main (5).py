def check0(L):
    if (len(L) == 0):
        return 0
    if (L[0] == 0):
        return 1
    else:
         return check0(L[1:len(L)])


L=[1,2,3,4,5,60,65,3]
ans = check0(L)
print(ans)
