def checkIfDivisor(dividend, divisor):
    """
    Check if a number is a divisor of another number by checking if
    the remainder of the the operation is 0.
    :param dividend: the number to divide
    :param divisor: the number to divide for
    :return: True if it's divisible or False if not
    """
    if dividend % divisor == 0:
        return True
    return False


if __name__ == '__main__':
    rangeNum = 100
    for num in range(1, rangeNum+1):
        strNum = str(num)
        containsThree = ('3' in strNum) or checkIfDivisor(num, 3)
        containsFive = ('5' in strNum) or checkIfDivisor(num, 5)
        if containsThree & containsFive:
            print("Fizz Buzz")
        else:
            if containsThree:
                print("Fizz")
            elif containsFive:
                print("Buzz")
            else:
                print(strNum)