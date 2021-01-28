# Crédito ao Bonieky Lacerda que desenvolveu esse código em JS e PHP.
# Eu apenas alterei para linguagem python.

def romanToInt(roman):
    n = 0
    romanNumbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(0, len(roman)):
        actualNumber = roman[i-1]
        nextNumber = roman[i]

        if nextNumber and romanNumbers[nextNumber] > romanNumbers[actualNumber]:
            n -= romanNumbers[actualNumber]
        else:
            n += romanNumbers[actualNumber]

    return n


romanNumber = str(input('Digite um numero romano: ')).upper()
print(f'{romanNumber} convertido para inteiro é: {romanToInt(romanNumber)}')
