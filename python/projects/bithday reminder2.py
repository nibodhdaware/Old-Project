
dict = {}

while True:
    print('_____Birthday Reminder_____')
    print('1. Show Birthday')
    print('2. Add Birthday')
    print('3. Exit')
    Choice = int(input('Choice: '))
    if Choice == 1:
        if len(dict) == 0:
            print('Nothing to show')
        else:
            name = input('Enter a Name: ')
            birthday = dict.get(name, "No data found")
            print(birthday)
    elif Choice == 2:
        name = input('Enter Name: ')
        date = input('Enter Birthdate: ')
        dict[name] = date
        print('Birthday Added')
    elif Choice == 3:
        print('======Exiting Program======')
        break
    else:
        print('Choose a valid option')