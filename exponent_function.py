def raise_to_power(base_num, pow_num):
    result_num = 1

    for p in range(pow_num):
        result_num *=  base_num
    return result_num


print(raise_to_power(2, 3))
