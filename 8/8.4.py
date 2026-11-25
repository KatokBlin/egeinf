from itertools import*
k=0
for i in product('0123456',repeat=6):
    s=''.join(i)
    if s[0]!='0' and s.count('6')==1:
        for c in '0246':
            s=s.replace(c,'*')
        for c in '135':
            s=s.replace(c,'!')
        if '**' not in s and '!!' not in s:
            k+=1
print(k)
