OldNode=['3', '6', '8', '10', '12','15', '18']
value=0
alternateNode=[]
newNode=[]
for i in range(len(OldNode)):
    for j in OldNode:
        value=value+int(j)
    alternateNode.append(int(OldNode[0]))
    OldNode.pop(0)
    newNode.append((value))
    value=value*0
print("This Old Node Value",(alternateNode))
print("This is New Node Value",newNode)