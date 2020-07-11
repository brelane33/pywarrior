def hex_output():
    decnum = 0
    hexnum = input('Enter a number in hexidecimal: ')
    print('\n')
    for power, digit in enumerate(reversed(hexnum)):
        print(f' The power is {power} and digit is {digit}')
        dec_value = int(digit, 16) * (16 ** power)
        print(f' The decimal value of this digit {dec_value}\n') 
        decnum += int(digit, 16) * (16 ** power)
    print (f'The total value is {decnum}')

def oct_output():
    decnum = 0
    octnum = input('Enter a number in octal: ')
    for power, digit in enumerate(reversed(octnum)):
        print(f' The power is {power} and digit is {digit}')
        octnum += int(digit, 8) * (8 ** power)
    print(decnum)

hex_output()
