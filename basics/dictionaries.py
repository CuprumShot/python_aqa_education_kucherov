'''
Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
'''


def phonebook_dict():
    phonebook = {
        'John': 938477566,
        'Jack': 938377264,
        'Jill': 947662781
    }

    # your code goes here
    phonebook.pop('Jill')
    phonebook['Jake'] = 938273443

    # testing code
    if 'Jake' in phonebook:
        print('Jake is listed in the phonebook.')

    if 'Jill' not in phonebook:
        print('Jill is not listed in the phonebook.')


if __name__ == '__main__':
    phonebook_dict()
