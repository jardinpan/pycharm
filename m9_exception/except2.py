try:
    num = int(input('enter a number:'))
    print('{}是一個{}'.format(num, '奇數' if num % 2 else '偶數'))
except ValueError:
    print('請輸入正整數')