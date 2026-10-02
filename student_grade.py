name= input("Enter Student's name: ")
score = int(input("Enter Student's score: "))

if score < 40:
    print("You got a F")
elif score >=40 and score <=44:
    print("You got an E")
elif score >=45 and score <=49:
    print("You got a D")
elif score >=50 and score <=59:
    print("you got a C")
elif score >=60 and score <=69:
    print("you got a B")
elif score >=70 and score <=100:
    print("you got an A")