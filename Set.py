#Set.py
"""s={10,20,30,40,50,10,30,50}
print(s,type(s))
for i in s:
	print(s,end="  ")"""

s={10,20,40,50,60,30,40,50}
fs=frozenset(s)
print(fs,type(fs))
for k in fs:
	print(k,end="       ")
