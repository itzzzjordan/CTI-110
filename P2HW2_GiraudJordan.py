# Jordan Giraud
# 9/25/23
# Introduction to lists

#Import the mem function
from statistics import mean

module_1=float(input("Enter a grade: "))
module_2=float(input("Enter a grade: "))
module_3=float(input("Enter a grade: "))
module_4=float(input("Enter a grade: "))
module_5=float(input("Enter a grade: "))
module_6=float(input("Enter a grade: "))

#Creat an empty list
test_grades=[]

#Add values in list
test_grades.append(module_1)
test_grades.append(module_2)
test_grades.append(module_3)
test_grades.append(module_4)
test_grades.append(module_5)
test_grades.append(module_6)


#Print all values in list
for grade in test_grades:
    print(grade)


print(f"The lowest grade is: {min(test_grades) :.1f}")

print(f"The highest grade is: {max(test_grades) :.1f}")

print(f"The sum of grade is: {sum(test_grades) :.1f}")

print(f"The average of grade is: {mean(test_grades) :.2f}")

