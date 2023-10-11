#Jordan Giraud
#10/11/23
#create and call a function





def leap_year_calc(input_year):
    
    is_leap_year = False


      

    if (input_year % 4) == 0:      # inputYear is divisible by 4

      if (input_year % 100) == 0:   # inputYear is divisible by 100 (century year)

        if (input_year % 400) == 0: # inputYear is divisible by 400

          is_leap_year = True

        else:           # inputYear is not divisible by 400

          is_leap_year = False

      else:             # inputYear is not divisible by 100

        is_leap_year = True

    else:               # inputYear is not divisible by 4

      is_leap_year = False

      

    if is_leap_year:

      return True

    else:

      return False


#main function starts here
def main():
    user_year = int(input("Enter a year: "))
    result = leap_year_calc(user_year)
    print(result)
    if result == True:
        print(f"{user_year} is a leap year")
    else:
        print(f"{user_year} is NOT a leap year") 

#call the main function
main()
 
