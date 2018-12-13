import os
annee=input("Saisissez une année : ")
annee=int(annee)

if annee%400 == 0 or (annee%4 == 0 and annee%100 !=0):
	print("L'année", annee,"est bisextille")
else:
	print("L'année", annee,"n'est pas une année bisextille")
os.system("pause")	
