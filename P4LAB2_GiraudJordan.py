#Jordan Giraud
#10/4/23
#intro to loops using range ()

int_1 = int(input("enter a num: "))
int_2 = int(input("enter a num: "))

#if first num is smaller 
if int_1 <= int_2:
    #execute for loop using range(start, stop, increment)
    for x in range(int_1, int_2+1, 5):
     print(x)

    

else:
    print("the first number must be smaller.")
