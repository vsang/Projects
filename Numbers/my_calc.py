if __name__ == '__main__':
    print "hello calc\n"
    try:
        n1 = raw_input("enter n 1:")
        n2 = raw_input("enter n 2:")
    except:
        print "stupid input"
    else:
        op = raw_input("+ - * / %:")
        if(op not in '+-*/%'):
            print "stupid input"
        else:
            print "%s %s %s = %s" % (n1, op, n2, eval(str(n1) + op + str(n2)))
