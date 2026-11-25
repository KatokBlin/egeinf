from itertools import*
k=0
for i in product(sorted('плюшка'),repeat=5):
    k+=1
    s=''.join(i)
    if s.count('ю')<=1 and 'шш' not in s:
        print(k)
