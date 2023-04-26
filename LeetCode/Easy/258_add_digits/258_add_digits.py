def addDigits_typeConversion(num: int) -> int:
    if num < 10:
        return num
    digits = [int(digit) for digit in str(num)]
    add = sum(digits)
    return addDigits_typeConversion(add)

def addDigits_noConversion(num: int) -> int:
    if num < 10:
        return num
    add = 0
    while num != 0:
        digit = num % 10
        add += digit
        num = (num - digit) // 10
    return addDigits_noConversion(add)
