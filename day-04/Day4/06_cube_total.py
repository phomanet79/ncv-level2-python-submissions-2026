
n = int(input(" Enter number: "))
total =0
k= 0
for x in range (1,n+1):
    cube = x**3
    k = k + 1
    total = total  + cube 
    print(k , "**" , cube)
   
print("Total = ", total)   