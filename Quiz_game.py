def greet():
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of questions.")
    print("Answer them correctly to score points."  )
    print("Instructions: Type Only True or False for each question.")
    print("Let's begin!\n")
    print("Plsease enter your name:")
    name = input()
    print(f"Hello, {name}! Good luck!\n")


def ask_question(question, answer):
    print(question)
    print("You have 10 seconds to answer this question.") 
    user_answer = input("Your answer (T/F or True/False): ").strip().lower()

    if user_answer in ['true', 't']:
        user_answer = "True"
    elif user_answer in ['false', 'f']:
        user_answer = "False"
    else:
        print("⚠️ Invalid input. Skipping question.\n")
        return False

    if user_answer == answer:
        print("✅ Correct!\n")
        return True
    else:
        print(f"❌ Wrong! The correct answer is {answer}.\n")
        return False


    
import random

import threading
def list_of_questions():
    question = [
    {"question": "The capital of France is Paris.", "answer": "True"},
    {"question": "The Python programming language was created by Guido van Rossum.", "answer": "True"},
    {"question": "The Earth has two moons.", "answer": "False"},
    {"question": "Water freezes at 0 degrees Celsius.", "answer": "True"},
    {"question": "The Great Wall of China is visible from the moon.", "answer": "False"},
    {"question": "The square root of 64 is 8.", "answer": "True"},
    {"question": "Lightning never strikes the same place twice.", "answer": "False"},
    {"question": "There are 365 days in a leap year.", "answer": "False"},
    {"question": "Venus is the closest planet to the Sun.", "answer": "False"},
    {"question": "Sound travels faster than light.", "answer": "False"}
]
    return question

ques=list_of_questions()
time_per_question = 10 #(s)timer for each quns
random.shuffle(ques)  # Shuffle the questions for randomness


def quiz_game():
    greet()
    questions = list_of_questions()
    score = 0
    for q in questions:

        timer = threading.Timer(time_per_question, lambda: print("Time's up!"))
        timer.start()
        if ask_question(question=q["question"], answer=q["answer"]):
            score += 1
        timer.cancel()
    else:
        print("Times UP!")
    
    print(f"🎯Quiz completed! Your final score is: {score}/{len(questions)}")
    score_calculator(score)



def score_calculator(score):
    if score >= 8:
        print("Excellent job! You scored:", score)
        print(f"You answered {score} out of 10 questions correctly.")
    elif score >= 5:
        print("Good job! You scored:", score)
        print(f"You answered {score} out of 10 questions correctly.")
    elif score >= 3:
        print("GO! and study GK you stupid. You scored:", score)
        print(f"You answered {score} out of 10 questions correctly.")
    else:
        print("Better luck next time! You scored:", score)       

def play_again():
    while True:
        print("Do you want to play again? (yes/no)")
        choice = input().strip().lower()
        if choice == 'yes':
            quiz_game()
        elif choice == 'no':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")        

#start game
quiz_game()   
play_again()         