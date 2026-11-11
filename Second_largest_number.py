array=[10,20,30,40,50]
sets=set()
for i in range(len(array)):
    if(max(array)>array[i]):
        sets.add(array[i])
print(array)
print("This is Second Largest number in array:",max((sets)))