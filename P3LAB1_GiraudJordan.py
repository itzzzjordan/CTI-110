# Jordan Giraud
#10/2/23
#using if statemnets to determine leap year

#get input from user

input_year = int(input("Enter a year: "))

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print("The year is a leap year")

        else:
            print("The year is NOT a leap year")

    else:
       print("The year is a leap year")

else:
    print("The year is NOT a leap year")
