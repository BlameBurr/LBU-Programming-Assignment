from random import choice, randrange
DISCONNECT_RATE = 0.1

if __name__ == '__main__':
    print("""Welcome to Pop Chat
One of our operators will be pleased to help you today.""")
    operator_name = choice(['Janice', 'Arthur', 'John', 'Jim', 'Simon', 'Anna', 'Ellie', 'Emily'])
    phrases = {
        'deadline': ['Your deadline has been extended by two working days.',
                     'I will speak to your course supervisor about getting an extension.'],
        'library': ['The library is closed today', 'The library is open right now.'],
        'wifi': ['WiFi is excellent across the campus.',
                 'Due to on-going maintenance, there are some WiFi issues currently.'],
        '': ['Hmm.', 'Tell me more.', 'Oh, I see.', 'I can see what you mean.']
    }
    exit_phrases = ['exit', 'quit', 'goodbye', 'see you soon', 'help']
    try:
        [username, domain] = input('Please enter your University of Poppleton email address: ').split("@")
        if domain != 'pop.ac.uk' or len(username) < 2:
            raise ValueError
    except ValueError:
        print('The email you entered was invalid, please try again later.')
        exit()

    print(f'Hi, {username}! Thank you, and Welcome to PopChat!')
    print(f'My name is {operator_name}, and it will be my pleasure to help you.')

    while True:
        if randrange(0, 100) < DISCONNECT_RATE*100:
            print('*** NETWORK ERROR ***')
            break
        question = input('---> ').lower()
        if not question:
            continue
        if question in exit_phrases:
            break

        for keyword in phrases.keys():
            if keyword in question:
                answer = (phrases.get(keyword))
                print(answer if type(answer) == 'str' else choice(answer))
                break
    print(f'Thanks, {username}, for using PopChat. See you again soon!')
