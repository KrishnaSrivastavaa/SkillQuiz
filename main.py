print("Welcome to Our Quiz...")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Thank you for playing!")
    quit()

score = 0
print("Let's Start.. Here are your questions for the Quiz")

answer = input("What is the full form of CPU? ")
if answer.lower() == "central processing unit":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

answer = input("What is the full form of RAM? ")
if answer.lower() == "random access memory":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

answer = input("What is the full form of HDD? ")
if answer.lower() == "hard disk drive":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

answer = input("What is the full form of SSD? ")
if answer.lower() == "solid state drive":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

print(f"Your got {score} questions correct")
print(f"You got " + str((score / 4) * 100) + "%.")


