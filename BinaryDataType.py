

def main():
    print('bytes, bytearray, memoryview')

    a = bytes(123)
    b = bytes('hi there', 'utf-8')
    c = bytes('GOODBYE', 'ascii')

    d = bytearray(123)
    e = memoryview(123)

    print('\na:', a)
    print(type(a))
    print('b:', b)
    print(type(b))
    print('c:', c)
    print(type(c))

    print('\nUpper function:')
    print(b.upper())
    print(c.upper())

    print('\nLower function:')
    print(b.lower())
    print(c.lower())

    print('\nIsupper function:')
    print(b.isupper())
    print(c.isupper())

    print('\nIslower function:')
    print(b.islower())
    print(c.islower())


if __name__ == '__main__':
    main()