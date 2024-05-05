import re
pattern=r'\d\.\d+'
s="I study Python every day"
print(re.match(pattern,s,re.I))
s2="3.11 Python I study every day"
print(re.match(pattern,s2))