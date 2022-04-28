class Response(Exception):
    pass


if __name__ == '__main__':
    print("""Stop! Who would cross the Bridge of Death
Must answer me these questions three, 'ere the other side he see.""")
    try:
        name = input('What is your name? ').lower()
        if name == 'arthur':
            raise Response('My Liege! You may pass!')
        if 'grail' not in input('What is your quest? ').lower().split():
            raise Response('Only those who seek the Grail may pass.')
        if input('What is your favourite colour? ')[0].lower() != name[0]:
            raise Response('Incorrect! You must now face the Gorge of Eternal Peril.')
        print('You may pass!')
    except Response as message:
        print(message)
