import questions
import random

while True:
    current_question = random.choice(questions.questions)
    print(current_question['question'])

    random.shuffle(current_question['answers'])
    answers = current_question['answers']

    for answer in range(len(answers)):
        print(f"{answer+1}. {answers[answer]}")

    try:
        selected_answer = int(input("Enter your answer: "))
    except ValueError:
        print("Error: invalid number")
        break
    
    try:
        if answers[selected_answer - 1] == current_question['correct']:
            print("You answered correctly!")
        else:
            print("Your answer wasn't correct. (womp womp)")
    except IndexError:
        print("Error: invalid answer")
        break
