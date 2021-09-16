
command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started!')
        else:
            started = True
            print('Car Started 🚗 ===>')
    elif command == 'stop':
        if not started:
            print('The car is already stopped!')
        else:
            started = False
            print('Car stopped 🚗 <==')
    elif command == 'help':
        print('''
start - to Start the car
stop - to Stop the car
quit - to quit the car
''')
    elif command == 'quit':
        break
        
    else:
        print("sorry, The machine does not understand your command 💻")