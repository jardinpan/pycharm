str = 'my wife is Uchida Maaya, Maayaaaaaaa'

print(str.find('Maaya'))
print(str.find('maaya'))
print(str.rfind('Maaya'))
print(str.count('Maaya'))
print(str.capitalize())
print(str.lower())
print(str.upper())
print(str.title())
print(str.swapcase())
print(str.replace('Maaya', 'maaya'))

str1 = '    LiSA    '
print(str1.lstrip())
print(str1.rstrip())
print(str1.strip())

str2 = 'ClariS'
width = 18
print(str2.center(width))
print(str2.ljust(width))
print(str2.rjust(width))