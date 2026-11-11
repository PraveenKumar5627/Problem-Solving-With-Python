k=int(input("Enter the K value:"))
digit_1=1
condition=True
while(condition):
    if(k%2==0 or k%5==0):
        print("K is even Number We Can't divided:",-1)
        condition=False
    elif(digit_1%k==0):
        print("This is Output of Smallest Divided By K:",len(str(digit_1)))
        print("This Single Digit Value:",digit_1)
        condition=False
    else:
        digit_1=digit_1*10+1
        