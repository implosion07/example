d=list()
f=open('file.txt','r')
for line in f:
    print(line)
    for w in line:
        if w in d or w.isalpha()!=True:
            continue
        d.append(w)
print(d)

