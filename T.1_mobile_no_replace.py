no1 = str(input("enter phone no.: "))
#print(no1)
a = no1.replace("-","")
no2 = a[::-1]
#print(no2)
no3 = no2[0:10]
no4 = str(no3) + "0"
#print(no3)
#print(no4)
no5 = no4[::-1]
print(no5)

