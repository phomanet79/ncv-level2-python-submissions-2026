mmarks = []
mark = int(input("enter marks: "))

while mark != -1:
    marks.append(mark)
    mark = int(input("enter marks: "))
   
print(f"our list has {len(marks)} elements")
 
for x in range(len(marks)):
    print(marks[x])
    
total = 0
for x in range(len(marks)):
    mark = marks[x]
    total = total + mark

avg = total/len(marks)
print(f'The sum of all marks = {total}')
print(f'The average of all marks = {avg}')
  