import os

year = input("Saisissez une année")

year = int(year)

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):

    print(year, "est bissextile")
else:
    print(year, "n'est pas bissextile")

os.sytem("pause")