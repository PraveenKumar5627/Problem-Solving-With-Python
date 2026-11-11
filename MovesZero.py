num=[0,0,0,1,0,0,0]
for i in num:
    if i==0:
        num.append(i)
        num.remove(i)
print(num)
