p=[1,2,3]
q=[1,2,4]
finding=False
for i in range(len(p)):
    if(p[i]==q[i]):
        finding=True
        
    else:
        finding=False
        break
print(finding)
        
