print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("That is not correct :( ")

answer = input("When was America discovered? ")

if answer.lower() == "1492":
    print("Correct!")
    score += 1
else:
    print("That is not correct :( ")

answer = input("At how many degrees the water boil? ")

if answer.lower() == "90":
    print("Correct!")
    score += 1
else:
    print("That is not correct :( ")

answer = input("What are the name of the 2 countries starting with letter Q and Y ")

if answer.lower() == "qatar and yemen":
    print("Correct!")
    score += 2
else:
    print("That is not correct :( ")

print()
print("You got " + str(score) + " questions correct, NICE TRY :)!")
print("You got " + str((score / 5) * 100) + "%.")
