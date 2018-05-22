def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)
    # for i in range(len(str(a))-1):
    #     return (a[-(len(str(b))):-1] == b)
