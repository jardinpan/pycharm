str1 = 'abc123'
print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit(), end='\n\n')

str2 = 'abc'
print(str2.isalnum())
print(str2.isalpha())
print(str2.isdigit(), end='\n\n')

str3 = '123'
print(str3.isalnum())
print(str3.isalpha())
print(str3.isdigit(), end='\n\n')

str4 = '_123'
print(str1.isidentifier())
print(str2.isidentifier())
print(str3.isidentifier())
print(str4.isidentifier(), end='\n\n')

str5 = 'Python'
print(str5.islower())
print(str5.isupper(), end='\n\n')

print(''.isspace())
print(' '.isspace())
print('\t'.isspace())
print('\n'.isspace(), end='\n\n')

str6 = 'xxx.py'
print(str6.startswith('x'))
print(str6.startswith('xx'))
print(str6.startswith('xy'))
print(str6.endswith('y'))
print(str6.endswith('.py'))