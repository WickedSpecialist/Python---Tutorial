
# dict():
#   d = {
#       'KEY': 'VALUE'
#   }


def main():
    print('dict:')

    d = dict()
    print('\nd:', d)
    print(type(d))

    countries = {
        'Asia': 'India',
        'Europe': 'Belgium',
        'Africa': 'Egypt',
        'America': 'Chile'
    }

    print('\ncountries:', countries)
    print('Europe:', countries['Europe'])

    print('\nItems function:')
    print('Items:', countries.items())

    print('\nKeys function:')
    print('Keys:', countries.keys())

    print('\nValues function:')
    print('Values:', countries.values())

    print('\nGet function:')
    print(countries.get('Africa'))

    print('\nPop function:')
    print(countries.pop('Africa'))

    print('\nPopitem function:')
    print(countries.popitem())


if __name__ == '__main__':
    main()