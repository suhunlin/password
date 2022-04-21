password = 'a123456'
count = 3
while count > 0:
    user_input = input('Please input password:')
    if password == user_input:
        print("Correct!!")
        break
    else:
        count -= 1
        print('Input error!!!You still have %d chance' %count)

