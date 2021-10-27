#marks obtained of a student in five different subjects such as:
phy=int(input("marks in phy"))
che=int(input("marks in che"))
mat=int(input("marks in mat"))
eng=int(input("marks in eng"))
lit=int(input("marks in lit"))

total=phy+che+mat+eng+lit

print("sum of all subjects is",total)

percentage=total/5

print("overall percentage of all subjects",percentage,"%")
