print("enter the marks obtained in 4 subject")
math=int(input("enter your marks in maths"))
english=int(input("enter your marks in english"))
science=int(input("enter your marks in science"))
hindi=int(input("enter your marks in hindi"))

total_marks=math+english+science+hindi
print(F"total marks obtained in all four subject is {total_marks}")

perc=(total_marks/400)*100
print(end="percentage marks=")
print(perc)