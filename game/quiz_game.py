# ----------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)

        guess = input("Enter One of the answer: ").upper()
        guesses.append(guess) 
        
        correct_guesses += chek_answer(questions.get(key), guess)
        question_num += 1 

    display_score(guesses, correct_guesses)    

# ----------------------
def chek_answer(answer, guess):

    if(answer == guess):
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# ----------------------
def display_score(guesses, result):
    print("------------------------")
    print("RESULTS")
    print("------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((result/len(questions))*100)     
    print("Your Score is: " + str(score) + "%" )
    play_again()
    


# ----------------------
def play_again():
    response = input("DO you want to playe again? (Yes/No) : ").upper()
    if response == 'YES' :
        new_game()
    else :
        print("Okay, Bye!")    

# created dictionary (key:value) pair 
questions = {
    "who created Python?: " : "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group? :": "C",
    "Is the Earth round? ": "A"
}

# to hold all sort of possible answer for the each question we use 2D list
# that represent possible answer for the paerticular question

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Mark ZuckerBurg", "D. Bill Gates"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Somosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. May be"]
          ]

new_game()

