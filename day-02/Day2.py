Num1 = int(input("Enter Number One: "))
Num2 = int(input("Enter Number Two: "))

if Num1 < Num2:
    SmallerNum = Num1
else:
    SmallerNum = Num2
    
HighestFactor = SmallerNum

while Num1 % HighestFactor  != 0 or Num2 % HighestFactor  != 0 :
    
    HighestFactor =  HighestFactor -1

print("The highest commom factor is " , HighestFactor)
