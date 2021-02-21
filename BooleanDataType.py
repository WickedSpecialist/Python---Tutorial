
# bool():
#     True, False


def main():
    print('bool:')

    a = True
    b = False

    print('\na:', a)
    print('\nb:', b)

    print('\nNOT keyword:')
    print('NOT a:', not a)
    print('NOT b:', not b)

    print('\nAND keyword:')
    print('a AND a:', a and a)
    print('a AND b:', a and b)
    print('b AND b:', b and b)

    print('\nOR keyword:')
    print('a OR a:', a or a)
    print('a OR b:', a or b)
    print('b OR b:', b or b)

if __name__ == '__main__':
    main()