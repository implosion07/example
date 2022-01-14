"""string manipulations"""
s="stark industres"
print(s[3],'\n',s[:10])
l=len(s)
for l in s:
    if(l==s):
        print(s)
print('ark' in s)
if s.startswith('sta') is True:
    s=s.upper()
    l=s.split()
    for letter in l:
        for j in letter:
            print(j,end='')
s=s.lower()
print(s.count('s'))
