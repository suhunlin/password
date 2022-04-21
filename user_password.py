password = 'a123456'
count = 3
while count > 0:
    count -= 1
    user_input = input('Please input password:')
    if password == user_input:
        print("Correct!!")
        break
    else:
        print('Input error!!!')
        if count > 0:
            print("You still have %d chance!!!" %count)

