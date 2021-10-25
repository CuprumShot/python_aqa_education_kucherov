'''
You will need to write a format string which prints out the data using the following syntax:
Hello John Doe. Your current balance is $53.44.
'''


def string_formatting():
    # final solution
    data = ('John', 'Doe', 53.44)
    format_string = 'Hello %s %s. Your current balance is $%s.'

    print(format_string % data)

    # alternative solutions

    # data = ('John', 'Doe', 53.44)
    # format_string = 'Hello'
    #
    # Solution number 1
    # print('%s %s %s. Your current balance is $%0.2f.' % (format_string, data[0], data[1], data[2]))
    #
    # Solution number 2
    # print(f'{format_string} {data[0]} {data[1]}. Your current balance is ${data[2]}.')


if __name__ == '__main__':
    string_formatting()
