print("This program calculates and displays travel expenses")

budget = int(input("Enter Budget:"))

destination = input("Enter your destination:")

gas = int(input("How much do you think you will spend on gas?"))

hotel = int(input("How much do you think you will spend on the hotel?"))

food = int(input("How much do you think you will spend on food?"))

print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print("\n")
print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food)
print("\n")
print("Remaining Balance:", budget-(gas+hotel+food))
