import random

def make_answer():
    ones_p = str(random.randint(0,9))
    while True:
        tens_p = str(random.randint(0,9))
        if tens_p != ones_p:
            break
    while True:
        hundreds_p = str(random.randint(0,9))
        if hundreds_p != ones_p and hundreds_p != tens_p:
            break
    return hundreds_p + tens_p + ones_p

def judge(guess, answer):
    ball = 0
    strike = 0
    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1

    if ball == 0 and strike == 0:
        return 'Out'
    if ball == 0:
        return f'{strike} Strike'
    if strike == 0:
        return f'{ball} Ball'
    return f'{ball} Ball {strike} Strike'

if __name__ == '__main__':
    pass
