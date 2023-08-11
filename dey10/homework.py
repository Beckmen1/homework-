#დავალება 1
child = int(input("რამდენი წლის ხარ: "))
mother = int(input("ramdeni wlis aris mamasheni: "))
if int(mother) > int(child*2):
    print("bingo") 
else:  
    print("mouse")


#დავალება 2
number = 0
while number <= 100:
    if number % 2 == 0:
        print(str(number) + " Even")
    else:
        print(str(number) + " Odd")
    number += 1


#დავალება 4

knowleage = input("სად სწავლობ")
num ="goashi"
if knowleage == num :
    print("you are a chead")
else:
    print("You have ruined your own future")


age =int(input("ramdeni wlis xar")) 
gender = int(input("male or famale"))
male = True
if age >65: 
    if gender == male:
        print("შენ გახვედი პენსიაზე")
    else:  
        print ("get out")



