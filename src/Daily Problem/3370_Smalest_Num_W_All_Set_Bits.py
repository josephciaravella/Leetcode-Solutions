import math as m

def smallestNumber(n):
    """
    :type n: int
    :rtype: int
    """
    res = m.log(n, 2)
    num = m.ceil(res)

    return int((2 ** (num+1))-1) if res == num else int((2 ** num)-1)

print(smallestNumber(4))


def smallestNumber2(n):
    s = bin(n)[2:]
    s = s.replace('0', '1')
    return int(s, 2)
