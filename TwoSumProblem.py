array=["10","20","30","40"]
duplicate=[]
target=50
added_value=0
finding= False
print(array)
for i in range(len(array)):
    for j in array:
        added_value=(added_value)+int(j)
        duplicate.append(j)
        if(target==added_value):
           added_value=added_value-int(j)
           print("This Index of Value to Added.. We get an Target Number:",end="")
           print([duplicate.index(str(added_value)),duplicate.index(j)])
        #  finding=True
        else:
            added_value=(added_value*0)+int(duplicate[i])
    array.pop(0)
    added_value=added_value*0
    if(finding):
        break
    
    
    
    
# --------------------------chatgpt code----------------------------------
# array=[10,20,30,40]
# target=50
# for i in range(len(array)):
#     for j in range(i+1,len(array)):
#         if(array[i]+array[j]==target):
#             print([array.index((array[i])),array.index(array[i+1])])
        
        
        