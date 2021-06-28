a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']
a3 = []
a3 = a1

def test(l1,l2):
    ans = []
    for i in l1:
        for j in l2:
            ans.append(i + j)
    return ans

print(test(a1, a2))
print(a3)