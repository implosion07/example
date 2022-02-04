import sympy as sp
import math
x=sp.symbols("x")
y=x**2+x+1
s=1
alp=int(input("ENTER ALPHA VALUE"))
while True:
  temp=s-alp*smp.diff(y,s)
  s=temp
  if math.fabs(s)<).000001:
    break
print("min value=",s)
