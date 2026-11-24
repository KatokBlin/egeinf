f=2**2045+2**1800-2**1000+4**700-2024
n=oct(f)[2::]
print(sum(int(i) for i in n))
