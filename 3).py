List1 = [11, 15, 6, 13, 13, 25, 32, 11, 20, 5, 31, 16, 32, 29, 11, 13, 3, 29, 28, 24]
List2 = [5, 19, 16, 4, 12, 7, 2, 28, 34, 29, 29, 36, 6, 8, 24, 18, 31, 7, 1, 7]



1.
List3 = List1 + List2
print(List3)

for i in List3:
    print("Listis on sarnaseid elemente")
    break
else:
    print("Sarnased elemendid puuduvad")
list_result = [i for i in List1 if i in List2]

print("Need on: ")
print(list_result)


    
2.
3.
List3 = List1 + List2
print(List3)

print("Listi kõige suurem number on: ")
print(max(List3))

print("Listi kõige väiksem number on: ")
print(min(List3))


4.
listSum = sum(List1)
listLenght = len(List1)
listAverage =listSum / listLenght
print("Esimese listi keskmine on: ")
print(listAverage)

listSum = sum(List2)
listLenght = len(List2)
listAverage =listSum / listLenght
print("Teise listi keskmine on: ")
print(listAverage)

5.
listSum = sum(List3)
listLenght = len(List3)
listAverage =listSum / listLenght
print("Mõlema listi keskmine on: ")
print(listAverage)

      




