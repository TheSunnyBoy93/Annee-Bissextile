import os
annee=input("Enter a year : ")
annee=int(annee)

if annee%400 == 0 or (annee%4 == 0 and annee%100 !=0):
	print("The year", annee,"is a leap year")
else:
	print("The year", annee,"isn't a leap year")
os.system("pause")	
