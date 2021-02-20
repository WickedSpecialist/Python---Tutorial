

def main():
    print('int, float, complex:')

    # int
    print('\nIntegers:')
    w = int()
    x = 12
    y = -5345
    z = x + 4 - y * 4
    print('w:', w, 'type:', type(w))
    print('x:', x, 'type:', type(x))
    print('y:', y, 'type:', type(y))
    print('z:', z, 'type:', type(z))

    # float
    print('\nFloating Numbers:')
    a = float()
    b = 3.23 * 4.56 - 5.2323
    e = 2.718
    p = 3.1415
    print('a:', a, 'type:', type(a))
    print('b:', b, 'type:', type(b))
    print('e:', e, 'type:', type(e))
    print('p:', p, 'type:', type(p))

    # complex
    print('\nComplex Numbers:')
    w = complex()
    x = 1 + 2j
    y = -5j
    z = 3.1415 - 2.718j
    print('w:', w, 'type:', type(w))
    print('x:', x, 'type:', type(x))
    print('y:', y, 'type:', type(y))
    print('z:', z, 'type:', type(z))

if __name__ == '__main__':
    main()
