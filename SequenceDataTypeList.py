
# list():
#     ['P', 'Y', 'T', 'H', 'O', 'N', 3]
#       0    1    2    3    4    5   6
#      -7   -6   -5   -4   -3   -2  -1


def main():
    print('list:')

    print('\nHere we create a list called fruits:')
    fruits = list()
    fruits = ['orange', 'banana', 'apple', 'papaya', 'pineapple', 'grapefruit', 'apple']
    print(fruits)
    print('Index 3:', fruits[3])
    print('Index -3:', fruits[-3])
    print('From 1 to 4:', fruits[1:5])
    print('From 1 to 6 with 2 steps:', fruits[1:7:2])

    print('\nAppend function:')
    fruits.append('tangerine')
    print(fruits)

    print('\nInsert function:')
    fruits.insert(3, 'tomato')
    print(fruits)

    print('\nCount function:')
    print(fruits.count('apple'))

    print('\nIndex function:')
    print(fruits.index('banana'))
    print(fruits.index('apple'))

    print('\nPop function:')
    print(fruits.pop(2))
    print(fruits)

    print('\nRemove function:')
    fruits.remove('banana')
    print(fruits)

    print('\nSort function:')
    fruits.reverse()
    print(fruits)

    print('\nReverse function:')
    fruits.reverse()
    print(fruits)

    listOfLists = [
        ['a', 'b', 'c', 'd', 'e', 'f'],
        [1, 2, 3, 4, 5, 6],
        [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    ]
    print('List of Lists:', listOfLists)

if __name__ == '__main__':
    main()