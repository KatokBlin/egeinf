from itertools import*
k=0
for i in product('0123456789abcdef',repeat=4):
    s=''.join(i)
    if s[0]!='0' and s.count('3')==1:
        f=0
        for c in range(3):
            if s[c]==s[c+1]:
                f=1
                break
        if not f:
            k+=1
print(k)
