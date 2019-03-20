coverage, area = eval(input('please input two numbers:'))
count = area // coverage
count += 0 if area % coverage == 0 else 1
unit = 'can' if count == 1 else 'cans'
print('Need %d %s to paint'%(count, unit))