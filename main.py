import module

print('숫자야구에 오신 것을 환영합니다!')

while True:
    answer = module.make_answer()
    while True:
        guess = input('> ')
        if guess == 'q':
            print('취소합니다.')
            break
        elif guess == answer:
            print('정답입니다!')
            break
        elif not guess.isdecimal():
            print('숫자가 아닙니다.')
        elif len(guess) != 3:
            print('세 자리가 아닙니다.')
        elif len(guess) != len(set(guess)):
            print('중복되었습니다.')
        else:
            print(module.judge(guess, answer))

    if input('--------------------\n다시 시작하시겠습니까? (y/n) ') == 'y':
        continue
    else:
        break