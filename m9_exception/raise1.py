try:
    num = int(input('Input a 0~100 score:'))
    if num < 0 or num > 100:
        raise ValueError
    print('Score is {}'.format(num))
except ValueError:
    print('Please input a 0~100 score')
