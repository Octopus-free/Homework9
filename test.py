test_string = ' 16 18'
test_number = 16

test_string.find(f' 18')

if f' {test_number} ' in test_string:
    print(f' {str(test_number)}')
    print('Число есть')
else:
    print('Числа нет')
    print(f' {str(test_number)}')