from itertools import*
k=0
for i in product(sorted('минус'),repeat=4):
    k+=1
    s=''.join(i)
    for c in 'мнс':
        s=s.replace(c,'*')
    for c in 'иу':
        s=s.replace(c,'!')
    if s.count('*')>=s.count('!'):
        print(k)
