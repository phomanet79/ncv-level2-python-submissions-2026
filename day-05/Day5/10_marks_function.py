def get_marks():
    marks = []
    mark = int(input("enter marks: "))
    while mark != -1:
        marks.append(mark)
        mark = int(input("enter marks: "))
    return marks 
    
def print_list_size(marks):
    print(f"our list has {len(marks)} elements")
    
def print_marks(marks):  
    for x in range(len(marks)):
        print(f'Mark {x+1} is {marks[x]}')

def get_sum_of_marks(marks):
   # sum = 0
    for x in range(len(marks)):
        mark = marks[x]
        sum = sum + mark
    return sum

def get_avg_of_marks(marks):
    total = 0
    for x in range(len(marks)):
        mark = marks[x]
        total = total + mark
        avg = total/len(marks)
        return avg

def get_highest_of_marks(marks):    
    highest_mark =0
    for j in range(len(marks)):
        if marks[j] > highest_mark:
            highest_mark = marks[j]
    return highest_mark
    
menu = 'Press 1 : capturing marks\n','Press 2 : check number of marks\n','Press 3 : To calculate sum of marks\n',
'Press 4 : To find highest mark\n','Press -1 : To exit\n'
print(menu)
while menu != -1:
    choice = int(input("Make your choice : "))
 
    entered_marks = []
    sum_mark = 0
    High_mark = 0
             
    if choice == 1:
        entered_marks = get_marks()
        print(entered_marks)       
    elif choice == 2:
        print_marks(entered_marks)

    elif choice == 3:
        print(get_sum_of_marks(entered_marks))
             
    elif choice == 4:
        print(get_highest_of_marks(entered_marks))
             
    elif choice == -1:            
        sys.exit()
             
#print(f'The sum of all marks = {total}')

#print(f'The average of all marks = {avg}')

#print(f'The highest mark of all marks = {highest_mark}')
