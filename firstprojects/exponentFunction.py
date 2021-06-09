def raise_to_power(num_base, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * num_base
    return result

print(raise_to_power(4, 8))