number = int(input("upto")) 
# x = input()
for n in range(1,number+1):
    for i in range(2,n+1):
        if n>1:
            if(n%i!=0 and n/i!=1):
                print(n)
            else:
                pass
        

    else:
        pass               
