
# range():
#    range(START, STOP, STEP)

def main():
    print('range:')

    a = range(10)
    print('\na:', a)
    print(type(a))

    b = range(24, 47)
    print('\nb:', b)
    print(type(b))

    c = range(24, 48, 4)
    print('\nc:', c)
    print(type(c))

    d = range(10)[3:8]
    print('\nd:', d)

    e = range(15, 45, 3)
    print('\ne:', e)

    print('\nStart of a range:', e.start)
    print('Step of a range:', e.step)
    print('Stop of a range:', e.stop)

    print('\nCount function:')
    print(e.count(21))
    
    print('\nIndex function:')
    print(e.index(24))


if __name__ == '__main__':
    main()