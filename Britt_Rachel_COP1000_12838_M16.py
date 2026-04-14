hits = 0
strikes = 0
userAnswer = ""
questions = ["What MLB Team Is In Tampa Bay?", "What MLB Team Is In Arlington?", "What MLB Team Is In Baltimore?", "What MLB Team Is In St. Louis?","What MLB Team Is In Detroit"]
answers = ["rays", "rangers", "orioles", "cardinals","tigers"]
numQuestions = len(questions) - 1 
currentQuestion = 0

print("Welcome to the Baseball Quiz!")
print("Answer the questions.")
print("3 ‘Strikes’ and you’re out! \n")

# loop through quiz
while strikes < 3 and currentQuestion <= numQuestions:
    # Prompt user and force lowercase for answer matching
    userAnswer = input(questions[currentQuestion] + "\nAnswer: ").lower() 

    # block executed if user provides correct answer
    if userAnswer == answers[currentQuestion]:
        print("Hit!\n")
        currentQuestion = currentQuestion + 1
        # increases correct answer count by 1
        hits = hits + 1 

    # block executed if user provides incorrect answer
    else:
        print("Strike!\n")
        currentQuestion = currentQuestion + 1
        # increase incorrect answer count by 1
        strikes = strikes + 1

# block executed if user incorrectly answered three questions
if strikes == 3:
    print("You're out!")
    print("You are " + str(hits) + " for " + str(currentQuestion) + "!")

# block executed if user successfully completed the quiz
else:
    print("Congrats!")
    print("You are " + str(hits) + " for " + str(currentQuestion) + "!")
