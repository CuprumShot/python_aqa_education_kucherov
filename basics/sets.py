'''
In the exercise below, use the given lists to print out a set containing all
the participants from event A which did not attend event B.
'''


def sets():
    a = ["Jake", "John", "Eric"]
    b = ["John", "Jill"]

    print(set(a).difference(set(b)))


if __name__ == '__main__':
    sets()
