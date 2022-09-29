# Write your code here :-)

import random, time
numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    print('#%s: %s x %s = ' % (questionNumber, num1, num2))
    wrong_count=0
    while True:
        ans = input()
        if int(ans) != num1*num2 and wrong_count<2:
            wrong_count += 1
            print('incorrect!!! try again')
            time.sleep(1)
        elif int(ans) != num1*num2 and wrong_count == 2:
            print('incorrect!!! next question')
            break
        else:
            print('correct')
            correctAnswers += 1
            time.sleep(1)
            break
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))

