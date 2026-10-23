
mark = float(input("Please enter mark : "))

while 0 < mark <= 100:
    if  80 <= mark <= 100 :
        print("Outstanding")
    else:
        if 70 <= mark <= 79:
             print("Highly competent")
        else:
            if  50 <= mark <= 69:
                print("competent")
            else:
                if 40 <= mark <= 49:
                    print("not yet competent")
                else:
                    print("Not achieved")
     
    break