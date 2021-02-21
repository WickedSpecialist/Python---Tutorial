
# tuple():
#     ('P', 'Y', 'T', 'H', 'O', 'N', 3)
#       0    1    2    3    4    5   6
#      -7   -6   -5   -4   -3   -2  -1

def main():
    print('tuple:')

    print('\nHere we create a tuple called countries:')
    countries = tuple()
    countries = ('france', 'germany', 'united kingdom', 'korea', 'japan', 'korea', 'russia')
    print(countries)
    print(type(countries))

    print('\nIndex 2:', countries[2])
    print('Index -3:', countries[-3])

    print('\nSubtuple:', countries[1:5])
    print('Subtuple with 2 steps:', countries[1:6:3])

    print('\nCount function:')
    print(countries.count('korea'))

    print('\nIndex function:')
    print('Index of "germany":', countries.index('germany'))
    print('Index of "korea":', countries.index('korea'))

    tupleOfTuples = (
        ('france', 'canada', 'japan', 'nigeria'),
        ('europe', 'america', 'asia', 'africa'),
        (1, 2, 3, 4)
    )
    print('\nTuple of Tuples:', tupleOfTuples)

if __name__ == '__main__':
    main()