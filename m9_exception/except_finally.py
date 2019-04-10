try:
    n1, n2 = eval(input('Enter two numbers to divide'))
    div = n1 / n2
    print('%d / %d = %s'%(n1, n2, div))
except ZeroDivisionError:
    print('Division by Zero')
except SyntaxError:
    print('Comma is missing')
except:
    print('Something wrong')
else:
    print('No exception')
finally:
    print('Must be done')


