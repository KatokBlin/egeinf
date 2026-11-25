from itertools import*
k=0
for i in product('0123456789abcde',repeat=5):
    s=''.join(i)
    if s[0]!='0' and s.count('8')==1:
        for c in 'abcde':
            s=s.replace(c,'*')
        if s.count('*')>=2:
            k+=1
print(k)
