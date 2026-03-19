hits = 0
strikes = 0
userAnswer = ""
questions = ["What MLB Team Is In Tampa Bay?", "What MLB Team Is In Arlington?", "What MLB Team Is In Baltimore?", "What MLB Team Is In St. Louis?","What MLB Team Is In Cincinnati"]
answers = ["rays", "rangers", "orioles", "cardinals","reds"]
numQuestions = len(questions) - 1
currentQuestion = 0

print("Welcome to the Baseball Quiz!")
print("Answer the questions.")
print("3 ‘Strikes’ and you’re out! \n")

while strikes < 3 and currentQuestion <= numQuestions:
    userAnswer = input(questions[currentQuestion] + "\nAnswer: ").lower()

    if userAnswer == answers[currentQuestion]:
        print("Hit!\n")
        currentQuestion = currentQuestion + 1
        hits = hits + 1

    else:
        print("Strike!\n")
        currentQuestion = currentQuestion + 1
        strikes = strikes + 1

if strikes == 3:
    print("You're out!")
    print("You are " + str(hits) + " for " + str(currentQuestion) + "!")

else:
    print("Congrats!")
    print("You are " + str(hits) + " for " + str(currentQuestion) + "!")
