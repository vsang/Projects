
def fac(n):
    if(n == 0):
        return 1
    else:
        return n * fac(n - 1)

if __name__ == "__main__":
    n = int(raw_input("asdf:"))
    print fac(n)
