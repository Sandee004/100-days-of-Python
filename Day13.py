course=input("Enter course name: ")
obtainable_score= int(input("Enter the maximum score attainable: "))
score= int(input("Enter your score: "))
percentage= (score/obtainable_score)*100
if percentage <= 50:
    print("You have a percentage of ", percentage, " and a grade D")
elif percentage >= 60 and percentage < 70:
    print("You have a percentage of ", percentage, " and a grade C")
elif percentage >= 70 and percentage < 80:
    print("You have a percentage of ", percentage, " and a grade of B")
elif percentage >= 80 and percentage < 90:
    print("You have a percentage of ", percentage, "and a grade of A-")
elif percentage >= 90 and percentage <=100:
    print("Brilliant!! You have a percentage of ", percentage, " and a grade of A+")