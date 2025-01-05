def reverseBits(n):
    # binary = bin(n)
    # bin_str = str(binary)
    # bin_str_list = list(bin_str)
    # reverse = bin_str_list[::-1]

    return int("{:032b}".format(n)[::-1], 2)