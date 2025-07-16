def dec2bin(x):
    quotient = x
    remainders = ""
    while (quotient > 0):
        print(quotient)
        if quotient % 2 == 0:
            remainders = remainders + '0'
        else: remainders = remainders + '1'
        quotient = quotient // 2

    print(remainders[::-1])

def main():
    dec2bin(16)

main()
