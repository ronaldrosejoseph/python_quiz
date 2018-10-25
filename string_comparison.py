# In compare function I'm expecting string with values not null
def compare(a, b):
    if a > b:
        return "Greater"
    elif b > a:
        return "Lesser"
    else:
        return "Equal"


def test_compare():
    test1 = True if "Lesser" == compare(5, 6) else False
    test2 = True if "Greater" == compare(9, 6) else False
    test3 = True if "Equal" == compare(5, 5) else False
    test4 = True if "Greater" == compare(5.5, 5) else False
    test5 = True if "Lesser" == compare(-5, 5) else False
    test6 = True if "Equal" == compare('5', '5') else False
    test7 = True if "Lesser" == compare('A', 'Z') else False

    print("test1 compare(5, 6): ",test1)
    print("test2 compare(9, 6): ",test2)
    print("test3 compare(5, 5): ",test3)
    print("test4 compare(5.5, 5): ",test4)
    print("test5 compare(-5, 5): ", test5)
    print("test6 compare('5', '5'): ", test6)
    print("test7 compare('A', 'Z'): ", test7)


test_compare()