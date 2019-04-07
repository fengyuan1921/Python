#!/usr/bin/env python
for a in range(1,10):
    for b in range(a,10):
        print("{}x{}={}\t".format(a,b,a*b))
    print("\n")

names = ['cali','lolo','haku']
ages = ['12','21','33']
for c in range(len(names)):
    print("{}'s age is {}".format(names[c],ages[c]))

print('\n')

for name,age in zip(names,ages):
    print("{}'s age is {}".format(name,age))