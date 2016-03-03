def intToRoman(num):
    roman_map = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    ]

    result = ''
    print roman_map
    for (roman, value) in roman_map:
        count = num / value
        print count, ' ', value
        if count:
            result, num = result + count * roman, num - count * value
        if not num:
            break

    return result

value = intToRoman(621)
print 'Result: ', value
