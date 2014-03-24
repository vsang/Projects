def bin2dec(b):
    dec = 0
    n = 0
    while (b > 0):
        last = b % 10
        dec += last * (2 ** n)
        b = b / 10
        n += 1
    return dec

if __name__ == "__main__":
    print bin2dec(1101)
