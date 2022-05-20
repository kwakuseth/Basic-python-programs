import math

print('Solving quadratic equations using The almighty formular')
a=float(input('What is a?'))
b=float(input('What is b?'))
c=float(input('What is c?'))
root=float(math.sqrt(b*b-(4.0*a*c)))
x1=float((-b+root)/2.0*a)
x2=float((-b-root)/2.0*a)
print('x = ',x1,' or x = ',x2)
