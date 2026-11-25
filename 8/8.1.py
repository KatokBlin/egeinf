from itertools import*
k=0
for i in product('012345678',repeat=7):
    if i[0] not in '01357':
        if int(i[-1])%3!=0:
            if i.count('6')>=1:
                k+=1
print(k)
