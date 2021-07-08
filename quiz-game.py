print("Welcome to my Python Quiz Game")

playing = input("Do you want to play? ")

# .lower() will convert text the user writes into lower case
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :D")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
else:
    print("Incorrect!")
