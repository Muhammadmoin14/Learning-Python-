
#! If Else Elif

#? Scenario: Movie Ticket Pricing

age = int(input("Enter your age: "))

if (age <= 5):
    print("Free Ticket for kids")
elif (age <= 12):
    print("Ticket price is $10")
elif (age <= 18):
    print("Ticket price is $15")
elif (age <= 60):
    print("Ticket price is $20")
else:
    print("Senior Citizen not allowed")

print("Thank you for using our service")