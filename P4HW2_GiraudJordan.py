

# Jordan Giraud
# 10/9/23


name = ""
count = 0
total_pay = 0
while name != "Done":

    name = input("enter employee name: ")
    if name != "Done":
        count = count + 1
        num_hours = float(input("enter numer of hours worked: "))
        pay_rate = float(input("enter hourly pay rate: "))
        OT_hours = 0
        has_OT = False
        OT_pay = 0


        #calculate overtime - yes/no - how much
        if num_hours > 40:
         has_OT = True
         OT_hours = num_hours - 40
        else:
         has_OT = False
        if has_OT == True:
         OT_pay = (pay_rate*1.5) * (num_hours - 40) #actual Ot total pay
        else:
         OT_pay = 0

         
        #calculate regular pay
        reg_pay = pay_rate * (num_hours - OT_hours)
        gross_pay = reg_pay + OT_pay
        total_pay = total_pay + gross_pay

        #display name, pay rate, number of hours worked, overtime hours, overtime pay, regular pay, gross pay
        print("Name: ", name)
        print("Overtime Hours: ", OT_hours)
        print("Overtime Pay: ", OT_pay)
        print("Regular Hours: ", num_hours - OT_hours)
        print("Regular Pay: ", reg_pay)
        print("Gross pay: ", reg_pay + OT_pay)

#While loop breaks
print ("Total number of employees entered:", count)
print("Total pay of employees: ", total_pay) 
