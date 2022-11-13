import random as r
print('Guess a number between 1 & 10')
answer = input()
answer = int(answer)
random = r.randint(1,10)
if answer == random:
    print('Correct!')
else:
    print('unlucky')
