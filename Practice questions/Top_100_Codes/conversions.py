def conversions(x):
    # x is in decimal
    print('Octal - {}'.format(oct(x))) # Decimal to octal
    binar = bin(x).replace('0b','')
    print('Binary - {}'.format(binar. rjust(8,'0'))) # decimal to binary
    print('Hexa-decimal - {}'.format(hex(x))) # decimal to hexa decimal
    
conversions(20)