

def main():
    print('Variables:')

    x = 'Hello, World'
    y = 123.234
    z = -3.1415

    a = x * 2
    b = y + z
    c = y ** z
    d = y % z
    e = y / z

    print('\na:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)
    print('e:', e)

    print('\nCircle Example:')
    pi = 3.1415
    
    radius_01 = 6
    circumference_01 = 2 * pi * radius_01
    surface_01 = pi * radius_01 * radius_01
    
    radius_02 = 13
    circumference_02 = 2 * pi * radius_02
    surface_02 = pi * radius_02 * radius_02
    
    print('1st Circle:')
    print('\tCircumference:', circumference_01, '\tSurface:', surface_01)
    print('2nd Circle:')
    print('\tCircumference:', circumference_02, '\tSurface:', surface_02)
    
if __name__ == '__main__':
    main()