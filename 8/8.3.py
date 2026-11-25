from itertools import*
k=0
for i in product('0123456789ab',repeat=6):
    s=''.join(i)
    if s[0]!='0' and s.count('b')==1 and s.count('0')+s.count('2')+s.count('4')+s.count('6')+s.count('8')+s.count('a')==s.count('1')+s.count('3')+s.count('5')+s.count('7')+s.count('9')+s.count('b'):
        k+=1
print(k)
