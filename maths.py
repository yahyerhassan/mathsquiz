
print('Been a long week? Lets keep that brain active! Welcome to the math quiz!')


import random 

random_number = random.randint(1,50)


def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*', '/'])
    
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    else:
        
        num2 = random.randint(1, 10)
        answer = round(num1 / num2, 2)  


    return f"What is {num1} {operation} {num2}?", answer

question, correct_answer = generate_question()
user_answer = input(question)




score = 0

if user_answer == float(correct_answer):
    print("Correct!")
    score += 1

else: 
    print(f"Incorrect. The correct answer is {correct_answer}.")



for i in range(10):
    question, correct_answer = generate_question()
    user_answer = input(question)
    
    if float(user_answer) == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer was {correct_answer}.")







if score == 10:

    print("PERFECT SCORE! 10/10 Absolute legend!")



elif score == 9:


    print("So close to perfect! 9/10 Brilliant work!")


elif score == 8:
 print("8/10! Really strong performance.")



elif score == 7:
    print("7/10! Solid effort, you clearly know your stuff.")




elif score == 6:
    print("6/10! Good work, just a bit more practice needed.")


elif score == 5:
    print("5/10! Right in the middle! Keep going!!")


elif score == 4:
    print("4/10! A few tricky ones there, keep practicing.")


elif score == 3:
    print("3/10! Rough round, but every attempt helps you improve.")


elif score == 2:
    print("2/10! Don't worry, maths clicks with more practice.")


elif score == 1:
    print("1/10! Everyone starts somewhere. Try again!")


else:
    print("0/10! Tough round, but you'll get there. Try again! It has been a long week, keep practicing and you'll improve!")



