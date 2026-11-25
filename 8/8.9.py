from itertools import*
k=0
for i in product(sorted('мизантроп'),repeat=5):
    k+=1
    s=''.join(i)
    if s[0]=='н' and s.count('р')==2 and k%2==0:
        print(k)
