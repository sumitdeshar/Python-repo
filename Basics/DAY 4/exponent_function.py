#print(2**4)#power of 2^4
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
    #print(result)
print(raise_to_power(7, 3))
#same code lekhda ne mildana tw bay