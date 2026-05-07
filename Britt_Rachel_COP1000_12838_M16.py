def NameTheTeam():
    hits = 0
    strikes = 0
    userAnswer = ""
    questions = ["What MLB Team Is In Tampa Bay?", "What MLB Team Is In Arlington?", "What MLB Team Is In Baltimore?", "What MLB Team Is In St. Louis?","What MLB Team Is In Detroit"]
    answers = ["rays", "rangers", "orioles", "cardinals","tigers"]
    numQuestions = len(questions) - 1 
    currentQuestion = 0
    
    print("You Chose Name The Team!")
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
        print("You are " + str(hits) + " for " + str(currentQuestion) + "!\n")

    # block executed if user successfully completed the quiz
    else:
        print("Congrats!")
        print("You are " + str(hits) + " for " + str(currentQuestion) + "!\n")
    
def NameThePlayer():    
    hits = 0
    strikes = 0
    userAnswer = ""
    questions = ["Who Is The Current Captain Of The Yankees?", "Who Is #13 On The Rays?", "Who Is The Current Star Pitcher On The Pirates?", "Who Is The Two-Way Star On The Dodgers","Who Is The Star Shortstop On The Royals"]
    answers = ["Aaron Judge", "Junior Caminero", "Paul Skenes", "Shohei Ohtani","Bobby Witt Jr"]
    numQuestions = len(questions) - 1 
    currentQuestion = 0
    
    print("You chose Name The Player!")
    print("Answer the questions.")
    print("3 ‘Strikes’ and you’re out! \n")

    # loop through quiz
    while strikes < 3 and currentQuestion <= numQuestions:
        # Prompt user and force a capital letter before each word for answer matching
        userAnswer = input(questions[currentQuestion] + "\nAnswer: ").title() 

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
        print("You are " + str(hits) + " for " + str(currentQuestion) + "!\n")

    # block executed if user successfully completed the quiz
    else:
        print("Congrats!")
        print("You are " + str(hits) + " for " + str(currentQuestion) + "! \n")

while True:
    print("Welcome to Baseball Quiz!")
    print("Select your quiz: \n 1. Name The Team \n or \n 2. Name The Player")
    choice = input ("Please choose either 1 or 2: ")

    if choice == "1":
        NameTheTeam()
        
    elif choice == "2":
        NameThePlayer()

    else:
        print("Please enter either 1 or 2")
