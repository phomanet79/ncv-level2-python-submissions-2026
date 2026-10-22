import math

side_a = float(input("Please enter Side a in metres): "))
side_b = float(input("Please enter Side b in metres): "))
if side_a <= 0:
    print("Side a must be greater than zero.")
    
if side_b <= 0:
    print("Side b must be greater than zero.")
        
hypotenuse = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))
print("Hypotenuse: ",f"{hypotenuse:.2f} m")
