
print('Been a long week? Lets keep that brain active! Welcome to the math quiz!')

  
import random
random_number = random.randint(1,9)

score = 0

question_1 = input('What is 8 + 5 ?')

if question_1 == '13':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is 13.')

question_2 = input('What is 12 - 7 ?')

if question_2 == '5':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is 5.')

question_3 = input('What is 9 x 3 ?')

if question_3 == '27':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is 27.')

question_4 = input('What is 15 ÷ 3 ?')

if question_4 == '5':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is 5.')

question_5 = input('What is 7 + 6 ?')

if question_5 == '13':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is 13.')

question_6 = input('What is 47 + 38 ?')

if question_6 == '85':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is 85.')

question_7 = input('What is 100 - 45 ?')

if question_7 == '55':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is 55.')

question_8 = input('What is 9 x 8 ?')

if question_8 == '72':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is 72.')

question_9 = input('What is 81 ÷ 9 ?')

if question_9 == '9':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is 9.')

question_10 = input('What is 14 + 9 ?')

if question_10 == '23':
    print('Correct!')
    score += 1
else:
    print('Incorrect. The correct answer is 23.')


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