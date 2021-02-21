
# set():
#     s = {
#         'VALUE_01', 'VALUE_02'
#     }


def main():
    print('set, frozenset:')

    a = set()
    b = {1, 2, 3, -4, 5, 5, 68, 4.5, -21, 'hello', 'goodbye'}
    c = frozenset(b)

    print('\na:', a)
    print('b:', b)
    print('c:', c)

    print('\nAdd function:')
    a.add(3.1415)
    a.add(-4)
    a.add(1)
    a.add('hello')
    print('a:', a)

    print('\nDifference function:')
    print(a.difference(b))
    print(b.difference(a))

    print('\nIntersection function:')
    print(a.intersection(b))
    print(b.intersection(a))

    print('\nPop function:')
    print(b.pop())
    print(b.pop())

    print('\nRemove function:')
    b.remove(68)
    print(b)

    print('\nUnion function:')
    print(a.union(b))

if __name__ == '__main__':
    main()