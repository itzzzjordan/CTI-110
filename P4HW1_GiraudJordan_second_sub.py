def num_to_letter(number):

   if number <= 100 and number >=90:

    letter = "A"

   elif number <= 89 and number >=80:

    letter = "B"

   elif number <= 79 and number >=70:

    letter = "C"

   elif number <=69 and number >=60:

    letter = "D"

   else:

    letter = "F"

     
   return letter



num_grades = int(input("How many grades will you enterz? "))
                 
grades_list = []
                 
for value in range (num_grades):
    grade = int(input(f"Enter grade #{value+1}: "))
    if grade >=0 and grade <=100:
        grades_list.append(grade)
    else:
        while grade < 0 or grade > 100:
            print("INVALID GRADE ENTERD!")
            print("Grade should be btween 0 and 100")
            grade = int(input(f"Re-enter grade #{vslue+1}:"))
        grades_list.append(grade)

min_grade = min(grades_list)

grades_list.remove(min_grade)

average = (sum(grades_list))/len(grades_list)

print("-----Results-----")
print("The lower grade is:", min_grade)
print(f"Grades after dropping lowest: {grades_list}")
print(f"Average: {average}")
print(f"Letter Grade: {num_to_letter(average)}")
