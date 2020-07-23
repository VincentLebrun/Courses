import os
from random import *
"""
i've imported some (functions) to use the random tools found here
https://docs.python.org/3/library/secrets.html#module-secrets"""

loto = []#i created a empty list tu full her by a random nums

for i in range (5):
# here i create a loop who take 5 number in list
    loto.append(randint(1,49))
#here it's to add some num in list so .append
nums = [0 for loto in range (5)]

loto2=[]
# i did the same to creat a complementary num like star in euromillions
for i in range (2):

    loto2.append(randint(1,12))

nums = [0 for loto in range (2)]

print (loto )

print (loto2)

os.system("pause")
