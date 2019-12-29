from re import search, findall


test_string = 'asd  +-+'
test_number = 6

if len(findall(r'[\d]', test_string)) == 0:
    print('цифры нет')
else:
    print('цифры есть')
